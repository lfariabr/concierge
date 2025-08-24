import streamlit as st
from services.deliveryService import get_lift_info, get_lift_info_from_db
import pandas as pd
from utils.alerts import send_discord_message
from helpers.hint import show_hints

def display():
    st.header("📦 Apt Lift Finder")
    apt = st.text_input("Enter the apartment number (e.g., 9.2.31):")

    # # DEBUG TOOL – See full table (optional toggle)
    # if st.checkbox("🔍 Show full apartment data (debug mode)"):
    #     df = pd.read_csv("data/apartments.csv")
    #     st.dataframe(df)

    if apt:
        message = f"A request for apartment {apt} was just sent."
        send_discord_message(message)
        # lift, notes = get_lift_info(apt.strip())
        lift, notes, hints = get_lift_info_from_db(apt.strip())
        if lift:
            notes_clean = notes.strip().lower() if notes else ""

            # === DELIVER TO DOOR ===
            if "deliver to door" in notes_clean:
                st.success(f"👉 **Deliver to door.**\n> Use **{lift}** for apartment **{apt}**")
                show_hints(hints)
                
            # === INFO FOR "STORE + DELIVER IF REQUESTED" ===
            elif "deliver if requested" in notes_clean:
                st.info(f"👉 {notes}\n> Use **{lift}** for apartment **{apt}**")
                show_hints(hints)
                
            # === NEUTRAL FOR "Store package and send notification" ===
            elif "store package and send notification" in notes_clean:
                st.info(f"👉 **Store the package** and send notification.\n> **{lift}** for apartment **{apt}**")
                show_hints(hints)

            # === FALLBACK FOR OTHER NOTES ===
            elif notes:
                st.info(f"Note: {notes}\n> Use **{lift}** for apartment **{apt}**")
                show_hints(hints)
                   
            else:
                st.info(f"📍 Use **{lift}** for apartment **{apt}**")
        else:
            st.error("Apartment not found.")
