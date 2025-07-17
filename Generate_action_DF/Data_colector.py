import requests
import pandas as pd
import yfinance as yf
from bs4 import BeautifulSoup

class Data_colector():

    
    _url = "https://www.fundamentus.com.br/resultado.php"
        

    def create_action_dataFrame(self,tickers):
        grup_data = pd.DataFrame()
        for ticker in tickers:
            action = yf.Ticker(f"{ticker}.SA")
            data = action.history(period="10y")
            data['Ticker'] = ticker
            grup_data = pd.concat([grup_data,data],ignore_index=True)

            
        return grup_data


    def get_tickers(self):    
        resp = requests.get(self._url, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]
        tickers = df['Papel'].tolist()
        return tickers