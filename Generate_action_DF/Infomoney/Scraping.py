import requests
import pandas as pd
import time
import numpy as np
from datetime import datetime


class Scraping():
    def __init__(self):
        self._headers = {
            "Accept-Language": "pt-BR",
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        } 
        self.delay = np.random.uniform(1,2)

    def make_markers(self):
        tikers = self._try_extract_tickers()
        if tikers is not None:
            for tiker in tikers:
                self._try_self_extract_markers(tiker)
                time.sleep(self.delay)
        else:
            print("Não foi possível gerar os dados")
    def _extract_markers(self,tiker):
        url = f"www.infomoney.com.br/{tiker}"
        resp = requests.get(url,headers=self.headers)
        """Em desenvolvimento"""
            
    def _try_extract_tickers(self):        
        try:
            return self._extract_tickers()
        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"{now}ERROR:{str(e)}")
            return None
                

    def _extract_tickers(self):
        data = self.try_get_tickers()        
        df_dados = pd.DataFrame(data)
        tikers = df_dados["StockCode"].to_list()
        return tikers

    def _try_get_data(self):
        try:
            return self.get_data()
        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"{now}ERROR:{str(e)}")
            return None

    def _get_data(self):
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
        





