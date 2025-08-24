import streamlit as st
from services.deliveryService import get_lift_info, get_lift_info_from_db
import pandas as pd
from utils.alerts import send_discord_message

def display():
    st.header("📦 Apt Lift Finder")
    apt = st.text_input("Enter the apartment number (e.g., 9.2.31):")

    # # DEBUG TOOL – See full table (optional toggle)
    # if st.checkbox("🔍 Show full apartment data (debug mode)"):
    #     df = pd.read_csv("data/apartments.csv")
    #     st.dataframe(df)

    if apt:
        message = f"A request for apartment {apt} was just sent."
        # send_discord_message(message)
        # lift, notes = get_lift_info(apt.strip())
        lift, notes = get_lift_info_from_db(apt.strip())
        if lift:
            notes_clean = notes.strip().lower() if notes else ""

            # === ✅ DELIVER TO DOOR ===
            if "deliver to door" in notes_clean:
                st.success(f"🚪 **You have to deliver this to door.**\n\nUse **{lift}** for apartment **{apt}**")

            # === ℹ️ INFO FOR "STORE + DELIVER IF REQUESTED" ===
            elif "deliver if requested" in notes_clean:
                st.info(f"📦 **{notes}**\n\nUse **{lift}** for apartment **{apt}**")

            # === ⚪ NEUTRAL FOR "Store package and send notification" ===
            elif "store package and send notification" in notes_clean:
                st.info(f"✅ **Store package and send notification. Easy**\n\nUse **{lift}** for apartment **{apt}**")

            # === ℹ️ FALLBACK FOR OTHER NOTES ===
            elif notes:
                st.info(f"ℹ️ Note: {notes}\n\nUse **{lift}** for apartment **{apt}**")

            # === NO NOTES, ONLY LIFT ===
            else:
                st.info(f"📍 Use **{lift}** for apartment **{apt}**")
        else:
            st.error("Apartment not found.")
