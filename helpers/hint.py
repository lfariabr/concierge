import streamlit as st

def show_hints(hints):
    if hints:
        st.warning(f"💡 **Hints:**\n{hints}")