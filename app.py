# app.py

import streamlit as st

# ---- Streamlit Config ----
st.set_page_config(
    page_title="Lift Finder",
    layout="centered",
    page_icon="🛎️",
    initial_sidebar_state="collapsed"
)

from views import rosterView, deliveryView, databaseView

# ---- App Title ----
st.title("Concierge Tool")
# st.markdown("Select a tool from the sidebar to get started.")
st.markdown("Use the tool below to optimize your delivery process.")

# ---- Sidebar Navigation ----
menu = st.sidebar.radio("📂 Select a screen:", [
    # "📅 Roster Availability",
    "📦 Apt Lift Finder",
    # "🗃️ Apt Database"
])

# ---- View Routing ----
if menu == "📅 Roster Availability":
    rosterView.display()

elif menu == "📦 Apt Lift Finder":
    deliveryView.display()

elif menu == "🗃️ Apt Database":
    databaseView.display()

# ---- Footer (Optional) ----
st.sidebar.markdown("---")
st.sidebar.caption("luisfaria.dev")
