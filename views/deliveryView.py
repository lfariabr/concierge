# views/deliveryView.py
import streamlit as st
from services.deliveryService import get_lift_info

def display():
    st.header("📦 Apartment Lift Finder")
    apt = st.text_input("Enter Apartment Number (e.g., 9.2.31):")

    if apt:
        lift, notes = get_lift_info(apt.strip())
        if lift:
            st.success(f"Use **{lift}** for apartment **{apt}**")
            if notes:
                st.info(f"Notes: {notes}")
        else:
            st.error("Apartment not found.")
