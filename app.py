# app.py

import streamlit as st
from views import rosterView, deliveryView

# ---- Streamlit Config ----
st.set_page_config(
    page_title="Lift Finder",
    layout="wide",
    page_icon="🛎️",
    initial_sidebar_state="collapsed"
)

# ---- App Title ----
st.title("Concierge Tool")
# st.markdown("Select a tool from the sidebar to get started.")
st.markdown("Use the tool below to optimize your delivery process.")

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
