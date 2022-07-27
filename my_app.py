
# Introduzione e plot di grafici di andamenti di borsa di una compagnia quotata

# Librerie
import streamlit as st
import pandas as pd
import yfinance as yf


st.write("""
         # Simple Stock Price App
         Shown are the stock **closing price** and ***volume*** of Eni!
         """)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'ENI.MI'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-6-24')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
         ## **Closing price**
         """)
st.line_chart(tickerDf.Close)

st.write("""
         ## **Volume price**
         """)
st.line_chart(tickerDf.Volume)
