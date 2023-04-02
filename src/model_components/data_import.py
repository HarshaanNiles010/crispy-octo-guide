import os
import sys
import yfinance as yf
from src.exception import CustomException
from src.logger import logging
""" ticker = yf.Ticker('GOOGL').info
market_price = ticker['regularMarketPrice']
previous_close_price = ticker['regularMarketPreviousClose']
print('Ticker: GOOGL')
print('Market Price:', market_price)
print('Previous Close Price:', previous_close_price) """

""" try:
    #comp_name = input("Enter the compnay ticker symbol(GOOGL): ")
    #ticker = yf.Ticker("GOOGL").info
    ticker = "GOOGL"
    start_date = '2021-01-01'
    end_date = '2022-01-01'
    data = yf.download(ticker, start_date, end_date)
    print(f"The company ticker being tracked is: {ticker}")
    print(data)
except Exception as e:
    raise CustomException(e,sys) """
    
class DataImportConfig():
    output_data_path: str = os.path.join('artifacts','tickerData.csv')

class DataImport():
    def __init__(self):
        self.data_import_config = DataImportConfig()
        
    def initiate_data_import(self):
        logging.info('Initializing data import')
        try:
            ticker = "GOOGL"
            start_date = '2022-01-01'
            end_date = '2023-01-01'
            logging.info(f"The ticker used is {ticker}, the start date is: {start_date} and the end date is: {end_date}")
            data = yf.download(ticker,start_date,end_date)
            #data["Index"] = data.index
            data = data[["Open", "High","Low", "Close", "Adj Close", "Volume"]]
            data.reset_index(drop=True, inplace=True)
            os.makedirs(os.path.dirname(self.data_import_config.output_data_path),exist_ok=True)
            data.to_csv(self.data_import_config.output_data_path,index=False,header=True)
            logging.info("Data successfully imported")
            return (
                self.data_import_config.output_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataImport()
    obj.initiate_data_import()