import requests
import pandas as pd
import time
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup


class Scraping():
    def __init__(self):
        self._headers = {
            "Accept-Language": "pt-BR",
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        } 
        self.delay = np.random.uniform(1,2)

    def make_markers_data(self):
        tikers = self._try(self._extract_tickers)
        if tikers is not None:
            for tiker in tikers:
                self._try(self._extract_markers,tiker)
                time.sleep(self.delay)
        else:
            print("Não foi possível gerar os dados")

    def _extract_markers(self,tiker):
        url = f"www.infomoney.com.br/{tiker}"
        resp = requests.get(url,headers=self._headers)
        soap = BeautifulSoup(resp.text,"html.parser" )
        markers = soap.find("table",class_="tables")


    def _extract_tickers(self):
        data = self._try(self._get_data)        
        df_dados = pd.DataFrame(data)
        tikers = df_dados["StockCode"].to_list()
        return tikers

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
        
    def _try(self,func,*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("log.txt", "a", encoding="utf-8") as log:
                log.write(f"{now}ERROR:{str(e)}")
            return None




