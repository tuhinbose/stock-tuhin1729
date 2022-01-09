import streamlit as st
import yfinance as finance


def get_ticker(name):
	company = finance.Ticker(name) # google
	return company


# Project Details
st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")
st.sidebar.header("Geeksforgeeks \n TrueGeeks")

company1 = get_ticker("IRCTC.NS")
company2 = get_ticker("INFY.NS")

# fetches the data: Open, Close, High, Low and Volume
google = finance.download("IRCTC.NS", start="2020-12-01", end="2021-01-08")
microsoft = finance.download("INFY.NS", start="2020-12-01", end="2021-01-08")

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")

# markdown syntax
st.write("""
### Google
""")

# detailed summary on Google
st.write(company1.info['longBusinessSummary'])
st.write(irctc)

# plots the graph
st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'], "\n", infosys)
st.line_chart(data2.values)
