from email.mime import image
import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np




st.title("Crypto Currency Prices.")
st.header(" Dashboard")

st.markdown("This application is a Crypto Currency Price dashboard : by Pratik Kadam")



bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XPR-USD'
BitcoinCash = 'BCH-USD'

BTC_Data = yf.Ticker(bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

BTHHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period='max')
XRPHis = XRP_Data.history(period='max')
BCHHis = BCH_Data.history(period='max')

BTC = yf.download(bitcoin, start="2021-1-1", end="2022-5-11")
ETH = yf.download(Ethereum, start="2021-1-1", end="2022-5-11")
XRP = yf.download(Ripple, start="2021-1-1", end="2022-5-11")
BCH = yf.download(BitcoinCash, start="2021-1-1", end="2022-5-11")


st.subheader("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
BTCplt = st.line_chart(BTHHis.Close)
st.header("Insight")
st.write('Bitcoin (₿) is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries')
st.dataframe(BTC)
st.write("")
st.write("")
st.write("") 

st.subheader("Ethereum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)
ETH_plot = st.line_chart(ETHHis.Close)
st.header("Insight")
st.write('Ethereum is a decentralized, open-source blockchain with smart contract functionality. Ether (ETH or Ξ) is the native cryptocurrency of the platform. Among cryptocurrencies, Ether is second only to Bitcoin in market capitalization')
st.dataframe(ETH)
st.write("")
st.write("")
st.write("")

st.subheader("Ripple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)
XRP_plot = st.line_chart(XRPHis.Close)
st.header("Insight")
st.write("Ripple is a technology that acts as both a cryptocurrency and a digital payment network for financial transactions. It was first released in 2012 and was co-founded by Chris Larsen and Jed McCaleb. Ripple's main process is a payment settlement asset exchange and remittance system, similar to the SWIFT system for international money and security transfers, which is used by banks and financial middlemen dealing across currencies.") 
st.dataframe(XRP)
st.write("")
st.write("")
st.write("")

st.subheader("BitcoinCash ($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
st.image(imageBCH)
XRP_plot = st.line_chart(BCHHis.Close)
st.header("Insight")
st.write("Bitcoin Cash (BCH) is a cryptocurrency that shares many of the same characteristics as Bitcoin (BTC) yet also integrates a number of changes and features that set it apart. It is considered a 'fork' of Bitcoin, although proponents argue that Bitcoin Cash more closely adheres to the original vision of creating a peer-to-peer electronic cash system as laid out in a 2008 white paper written by the founder of the protocol, a person or group going by the pseudonym Satoshi Nakamoto. ")
st.dataframe(BCH)










# pipenv shell
# streamlit run Dashboard.py