import sys
import yfinance as yf
from src.exception import CustomException
""" ticker = yf.Ticker('GOOGL').info
market_price = ticker['regularMarketPrice']
previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Market Price:', market_price)
print('Previous Close Price:', previous_close_price) """

try:
    comp_name = input("Enter the compnay ticker symbol(GOOGL): ")
    ticker = yf.Ticker(comp_name).info
    market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']
except Exception as e:
    raise CustomException(e,sys)