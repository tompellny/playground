import streamlit as st
import numpy as np
import pandas as pd

st.title("🧪 TA-Lib Test: Simple Moving Average")

# --- Try importing TA-Lib ---
try:
    import talib
    st.success("✅ TA-Lib successfully imported!")
except Exception as e:
    st.error(f"❌ TA-Lib import failed: {e}")
    st.stop()

# --- Generate random data ---
np.random.seed(42)
close = np.random.random(100) * 100  # 100 random 'price' points

# --- Calculate SMA ---
timeperiod = 10
sma = talib.SMA(close, timeperiod=timeperiod)

# --- Create a DataFrame for plotting ---
df = pd.DataFrame({
    'Price': close,
    f'SMA({timeperiod})': sma
})

st.line_chart(df)

st.write("✅ Chart shows random data (blue) and SMA (orange).")
st.write("TA-Lib version:", talib.__version__)
