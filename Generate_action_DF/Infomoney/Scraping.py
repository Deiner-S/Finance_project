import requests
import pandas as pd
import time
import numpy as np
from ErroExtractData import ErroExtractData


class Scraping():
    def __init__(self):
        self._headers = {
            "Accept-Language": "pt-BR",
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        } 
        self.delay = np.random.uniform(1,2)

    def markers(self):

        for tiker in tikers:
            url = "www.infomoney.com.br/{tiker}"
            resp = requests.get(url,headers=self.headers)
            time.sleep(self.delay)

            
    def extract_tickers(self):
        data = self.try_get_tickers()

        if data == None or data is not dict:
            raise ErroExtractData()
        
        df_dados = pd.DataFrame(data)
        tikers = df_dados["StockCode"].to_list()

    def try_get_data(self):
        try:
            return self.get_data()
        except Exception as e:
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(str(e))
                print("Data")
            return None

    def get_data(self):
        url = f"https://api.infomoney.com.br/ativos/top-alta-baixa-por-ativo/acao?sector=Todos&orderAtributte=Volume&pageIndex={page}&pageSize=15&search="
        data = []
        page = 1   
        while True: 
            resp = requests.get(url,headers=self.headers)
            if resp.status_code != 200 or not resp.json():
                break            
            data.extend(resp.json()["Data"])
            page += 1
            time.sleep(self.delay)
        
        return data
        





