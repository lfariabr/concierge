import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import gspread
import json
from google.oauth2.service_account import Credentials

def display():
    st.header("📦 Apartments Database")

    try:
        # Get credentials from secrets
        credentials = json.loads(st.secrets["gsheets"]["credentials"])
        spreadsheet_url = st.secrets["gsheets"]["spreadsheet_url"]
        
        # Configure credentials
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        
        credentials = Credentials.from_service_account_info(
            credentials,
            scopes=scope
        )
        
        # Create client
        client = gspread.authorize(credentials)
        
        # Open spreadsheet
        apartments_sheet = client.open_by_url(spreadsheet_url)
        apartments_worksheet = apartments_sheet.worksheet("Apartments")
        apartments_data = apartments_worksheet.get_all_values()
        
        if not apartments_data:
            st.warning("No data found in the spreadsheet!")
            st.stop()
        
        df_apartments = pd.DataFrame(apartments_data[1:], columns=apartments_data[0])

        st.dataframe(df_apartments)
        
        # # Add form for grocery expense input
        # with st.form("grocery_form"):
        #     col1, col2, col3 = st.columns([2, 2, 1])
            
        #     with col1:
        #         operation = st.selectbox(
        #             "Operation",
        #             options=["Remove", "Add"],
        #             help="Select whether to add or remove amount"
        #         )
            
        #     with col2:
        #         amount = st.number_input("Amount", 
        #                             min_value=0.01, 
        #                             step=0.01,
        #                             help="Enter the amount")
            
        #     with col3:
        #         submitted = st.form_submit_button("Submit")
            
        #     if submitted:
        #         try:
        #             # Get current date
        #             current_date = pd.Timestamp.now().strftime('%Y-%m-%d')
                    
        #             # Determine final amount based on operation
        #             final_amount = amount if operation == "Add" else -amount
                    
        #             # Update the spreadsheet with values in a range
        #             apartments_worksheet.append_row([final_amount, current_date])
                    
        #             st.success(f"{operation}ed amount: {final_amount}")
        #             st.rerun()
                    
        #         except Exception as e:
        #             st.error(f"Error updating amount: {str(e)}")

        # # Display dataframe inverted with recent transactions on top
        # if not df_apartments.empty:
        #     df_apartments = df_apartments.sort_index(ascending=False)
            
        #     # Get the actual column names from the dataframe
        #     amount_column = df_apartments.columns[0]  
        #     date_column = df_apartments.columns[1]    
        
        #     # Convert amount column to numeric for calculations
        #     df_apartments[amount_column] = pd.to_numeric(df_apartments[amount_column], errors='coerce')
            
        #     # Get column names
        #     current_column = df_apartments.columns[2]  # Third column (C) should be "Current"
            
        #     # Calculate metrics
        #     total_spent = abs(df_apartments[df_apartments[amount_column] < 0][amount_column].sum())  # Sum of negative values
        #     current_balance = pd.to_numeric(df_apartments[current_column].iloc[-1], errors='coerce')  # Last value from Current column
            
        #     # Display metrics in columns
        #     col1, col2 = st.columns(2)
        #     with col1:
        #         st.metric("Total Spent on apartments", f"${total_spent:.2f}")
        #     with col2:
        #         st.metric("Current Balance", f"${current_balance:.2f}")
            
        #     # Display the transactions
        #     st.subheader("Recent Transactions")
        #     st.dataframe(df_apartments, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please check your Google Sheets credentials and connection.")