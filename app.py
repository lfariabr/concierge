# app.py

import streamlit as st
from views import rosterView, deliveryView

# ---- Streamlit Config ----
st.set_page_config(
    page_title="Concierge Dashboard",
    layout="wide",
    page_icon="🛎️",
    initial_sidebar_state="collapsed"
)

# ---- App Title ----
st.title("Concierge Tools ")
st.markdown("Select a tool from the sidebar to get started.")

# ---- Sidebar Navigation ----
menu = st.sidebar.radio("📂 Select a screen:", [
    # "📅 Roster Availability",
    "📦 Apartment Lift Finder"
])

# ---- View Routing ----
if menu == "📅 Roster Availability":
    rosterView.display()

elif menu == "📦 Apartment Lift Finder":
    deliveryView.display()

# ---- Footer (Optional) ----
st.sidebar.markdown("---")
st.sidebar.caption("Built by luisfaria.dev 🚀")
