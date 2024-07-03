import streamlit as st
import pandas as pd

# Set up the layout
st.set_page_config(layout="wide")

# Mock data
account_balance = 68789.56
accounts = [
    {"name": "Santander", "balance": 12220.65},
    {"name": "CityBank", "balance": 25070.65},
    {"name": "Deutsche Bank", "balance": 570.00},
    {"name": "Credit Agricole", "balance": 2680.50},
]

transactions = [
    {"date": "Today", "description": "Starbucks Cafe", "type": "Card payment", "category": "Food", "amount": -15.00},
    {"date": "Today", "description": "Off White Oxford Street 41", "type": "Card payment", "category": "Clothes", "amount": -260.40},
    {"date": "20.05", "description": "Spotify Premium", "type": "Fee", "category": "Entertainment", "amount": -10.00},
    {"date": "20.05", "description": "Google Inc.", "type": "Transfer", "category": "Salary", "amount": 9500.00},
    {"date": "19.05", "description": "Allegro.pl Sp.z.o.o", "type": "Blik", "category": "Clothes", "amount": -25.67},
    {"date": "19.05", "description": "Super-Pharm Warsaw", "type": "Blik", "category": "Pharmacy", "amount": -98.90},
    {"date": "18.05", "description": "Carrefour Express", "type": "Card payment", "category": "Food", "amount": -45.78},
]

expenses = {
    "daily": 275.40,
    "weekly": 1420.65,
    "monthly": 8200.00,
    "categories": {
        "Entertainment": 8400,
        "Clothes": 3000,
        "Bills": 2000,
        "Health": 1500,
        "Education": 1000,
        "Other": 800,
    }
}

# Main Account Balance
st.title("NevBank Dashboard")
st.subheader("Main Account")
st.metric(label="NevBank Savings Account", value=f"${account_balance:,.2f}")

# Accounts
st.subheader("Accounts")
cols = st.columns(len(accounts))
for i, account in enumerate(accounts):
    with cols[i]:
        st.metric(label=account["name"], value=f"${account['balance']:,.2f}")

# Latest Transactions
st.subheader("Latest Transactions")
df_transactions = pd.DataFrame(transactions)
st.table(df_transactions)

# All Expenses
st.subheader("All Expenses")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Daily", value=f"${expenses['daily']:,.2f}")
    st.metric(label="Weekly", value=f"${expenses['weekly']:,.2f}")
    st.metric(label="Monthly", value=f"${expenses['monthly']:,.2f}")

# Expense Categories
with col2:
    st.write("Expense Categories")
    df_expenses = pd.DataFrame(list(expenses["categories"].items()), columns=["Category", "Amount"])
    st.bar_chart(df_expenses.set_index("Category"))

# Run the app with: streamlit run app.py
