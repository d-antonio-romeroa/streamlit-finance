


import streamlit as st
from yfinance import Ticker
import pandas as pd
import plotly.graph_objects as go

# Custom functions
from data_processing import get_stock_data, generate_signals, plot_stock

# Streamlit App
st.title("Stock Trading Web App")

# Input for stock ticker
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):")

if ticker:
    # Fetch and process stock data
    data = get_stock_data(ticker)
    data = generate_signals(data)

    # Show basic data summary
    st.write(f"Showing data for: **{ticker}**")
    st.write(data.tail())  # Display the last 5 rows of data

    # Plot the stock data
    fig = plot_stock(data, ticker)
    st.plotly_chart(fig)

    # Show Buy/Sell signals
    st.subheader("Buy/Sell Signals")
    signal_counts = data['Signal'].value_counts()
    st.write(f"Buy signals: {signal_counts.get(1, 0)}, Sell signals: {signal_counts.get(-1, 0)}")