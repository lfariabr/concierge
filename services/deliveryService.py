import csv
import gspread
import json
from google.oauth2.service_account import Credentials
import streamlit as st

def get_lift_info(apartment_number: str):
    """
    Fetch lift information for a given apartment number from a CSV file.
    Returns the lift number and any associated notes.
    """
    with open("data/apartments.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Apartment"] == apartment_number:
                return row["Lift"], row.get("Notes", "")
    return None, None

def get_lift_info_from_db(apartment_number: str):
    """
    Fetch lift information for a given apartment number from the Google Sheets database.
    Returns the lift number and any associated notes.
    """
    # Get credentials and spreadsheet URL from Streamlit secrets
    credentials = json.loads(st.secrets["gsheets"]["credentials"])
    spreadsheet_url = st.secrets["gsheets"]["spreadsheet_url"]

    # Set up Google Sheets API credentials
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    credentials = Credentials.from_service_account_info(credentials, scopes=scope)
    client = gspread.authorize(credentials)

    # Open the spreadsheet and worksheet
    apartments_sheet = client.open_by_url(spreadsheet_url)
    apartments_worksheet = apartments_sheet.worksheet("Apartments")
    apartments_data = apartments_worksheet.get_all_values()

    # Convert to list of dicts for easy lookup
    if not apartments_data or len(apartments_data) < 2:
        return None, None
    headers = apartments_data[0]
    for row in apartments_data[1:]:
        row_dict = dict(zip(headers, row))
        if row_dict.get("Apartment") == apartment_number:
            return row_dict.get("Lift"), row_dict.get("Notes", "")
    return None, None