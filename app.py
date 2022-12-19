import streamlit as st
import yfinance as yf
import pandas as pd #for displaying data as table
import cufflinks as cf #for plots
import datetime

st.markdown('''
STOCK PRICE APP
''')

st.write('---')

st.sidebar.subheader('Query Parameters')
start_date=st.sidebar.date_input("Start Date",datetime.date(2020,1,1,))
end_date=st.sidebar.date_input("End Date",datetime.date(2023,1,31))

ticker_list=pd.read_csv('list.txt')
tickerSymbol=st.sidebar.selectbox('Stock ticker',ticker_list)
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start=start_date,end=end_date)

string_logo='<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name=tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary=tickerData.info['longBusinessSummary']
st.info(string_summary)

st.header('**Ticker data**')
st.write(tickerDf)

st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)