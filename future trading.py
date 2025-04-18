import streamlit as st

st.set_page_config(page_title="Futures Risk Calculator", layout="centered")

st.title("📉 Futures Trading Calculator")
st.caption("Made by Yadu 💻")

# Input section
entry_price = st.number_input("Entry Price", value=60000)
leverage = st.slider("Leverage (x)", 1, 125, value=10)
position_type = st.radio("Position Type", ["Long", "Short"])
account_balance = st.number_input("Account Balance ($)", value=1000)
risk_percent = st.slider("Risk Per Trade (%)", 1, 100, 2)
stop_loss_percent = st.slider("Stop Loss Distance (%)", 1, 100, 5)
target_move_percent = st.slider("Target Price Move (%)", 1, 100, 10)

# Calculations
if position_type.lower() == 'long':
    liquidation_price = entry_price - (entry_price / leverage)
else:
    liquidation_price = entry_price + (entry_price / leverage)

risk_amount = (account_balance * risk_percent) / 100
position_size = risk_amount / (stop_loss_percent / 100)
pnl = (target_move_percent / 100) * position_size * leverage

# Output
st.markdown("### 📊 Result Summary:")
st.success(f"💥 Liquidation Price: ${liquidation_price:,.2f}")
st.info(f"📏 Position Size: ${position_size:,.2f}")
st.warning(f"⚠️ Risk Amount: ${risk_amount:,.2f}")
st.success(f"🚀 Potential Profit (if target hit): ${pnl:,.2f}")
