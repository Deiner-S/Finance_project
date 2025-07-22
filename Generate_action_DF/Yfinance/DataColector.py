import requests
import numpy as np
import logging
import time
import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup

class DataColector():

    def __init__(self):
        self._url = "https://www.fundamentus.com.br/resultado.php"
    
    
        

    def grup_action_data(self):
        self._logging()
        grup_data = pd.DataFrame()
        tickers_list = self._get_tickers()
        for ticker in tickers_list:
            new_data = self._search_action(ticker)
            if new_data is not None:
                grup_data = pd.concat([grup_data,new_data],ignore_index=True)  
            delay = np.random.uniform(1,3)
            time.sleep(delay)         
        return grup_data
    
    def _logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('log.txt', mode='a', encoding='utf-8'),
                logging.StreamHandler()
                ]
        )


    def _search_action(self, ticker):
        action = yf.Ticker(f"{ticker}.SA")
        data = action.history(period="10y")
        data['Ticker'] = ticker
        return data

    def _get_tickers(self):    
        resp = requests.get(self._url, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]
        tickers = df['Papel'].tolist()
        return tickers