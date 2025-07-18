import requests
import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup

class Data_colector():

    
    _url = "https://www.fundamentus.com.br/resultado.php"
        

    def grup_action_data(self):
        grup_data = pd.DataFrame()
        tickers_list = self._get_tickers()
        for ticker in tickers_list:
            new_data = self._try_search_action(ticker)
            grup_data = pd.concat([grup_data,new_data],ignore_index=True)           
        return grup_data
    
    def _try_search_action(self,ticker):
        try:
            return self._search_action(ticker)
        except Exception as e:
            with open("log.txt", "a") as log:
                log.write(e)
            return None

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