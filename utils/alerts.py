import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # load .env if present

def _get_webhook_url():
    # Try Streamlit secrets first
    try:
        if "discord" in st.secrets and "webhook_url" in st.secrets["discord"]:
            return st.secrets["discord"]["webhook_url"]
    except Exception:
        pass
    # Fallback to env var
    return os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(message: str) -> int:
    url = _get_webhook_url()
    if not url:
        raise RuntimeError(
            "Discord webhook not configured. "
            "Add [discord].webhook_url to .streamlit/secrets.toml "
            "or set DISCORD_WEBHOOK_URL in your environment."
        )

    payload = {"content": (message or "")[:2000]}  # Discord max 2000 chars
    r = requests.post(f"{url}?wait=true", json=payload, timeout=10)

    # Handle rate limiting (429)
    if r.status_code == 429:
        retry_after = r.headers.get("Retry-After")
        if retry_after:
            time.sleep(float(retry_after))
            r = requests.post(f"{url}?wait=true", json=payload, timeout=10)

    r.raise_for_status()
    return r.status_code
