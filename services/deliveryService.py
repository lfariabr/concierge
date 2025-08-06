import csv

def get_lift_info(apartment_number: str):
    with open("data/apartments.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Apartment"] == apartment_number:
                return row["Lift"], row.get("Notes", "")
    return None, None
