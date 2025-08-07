# 🏢 Apartment Lift Finder

Welcome to the **Apartment Lift Finder** — a super simple, fast, and intuitive tool built to help concierge staff, building managers, and delivery personnel **instantly find which lift to use** for any apartment in the building.

---

## 🚀 What is this?

Too often, we were losing valuable time trying to remember which lift served which apartment — and more importantly, whether we needed to **deliver to the door** or **just store the package**.

So we fixed it.

This app was created to solve that exact pain point. Type the apartment number (e.g., `9.2.31`), and instantly get:

✅ The correct **Lift number**  
📍 Any **special delivery notes**  
⚠️ Highlighted actions like **"Deliver to Door"** or **"Store & Notify"**

---

## 🎯 Why we built this

> "I was spending 5-10 minutes per delivery looking this up, asking around, or double-checking. Now it takes 5 seconds."  
> — **Luis**, Casual Concierge & Builder of the Tool

What started as a personal helper evolved into something that's now used by our whole team — and could be adapted to any residential building or delivery operation.

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** – Python-based UI for rapid prototyping  
- **CSV-based data** – Simple data model for lifts, apartments, and delivery instructions  
- **Layered Architecture**:
  - `views/` for front-end logic  
  - `services/` for business logic (e.g., lift lookup)  
  - `data/apartments.csv` for structured building data

---

## 📦 How to Use

1. Open the app: [https://excelbm-swharf.streamlit.app/](https://excelbm-swharf.streamlit.app/)
2. Enter the apartment number (e.g., `8.5.34`)
3. Done ✅

You'll get:
- The correct **Lift**
- Any **special instructions**
- Clear color-coded actions (e.g., green for "Deliver to Door")

---

## 📁 Example CSV structure

```csv
Lobby,Lift,Apartment,Notes
Lobby 1,Lift 8.1,8.1.01,
Lobby 1,Lift 9.2,9.1.07,Deliver to Door
Lobby 2,Lift 8.5,8.2.39,Store package and send notification
```

--- 

## 💡 Possible Improvements
- Admin interface to edit or upload CSV data
- Apartment autocomplete
- Mobile-friendly view
- Integration with existing building systems (e.g., B/L, intercom or mail logs)
