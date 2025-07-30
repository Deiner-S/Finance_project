import requests
import pandas as pd
import time
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup
import os
from Exceptions.no_data import NoData

class Scraping():
    def __init__(self):
        self._headers = {
            "Accept-Language": "pt-BR",
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        } 
        self._delay = np.random.uniform(1,2)

    def run(self):
        try:
            self._make_indicators_data()
        except Exception as e:
            day = datetime.now().strftime("%Y-%m-%d")
            hours = datetime.now().strftime("%H:%M:%S")            
            with open(self._log_path(f"{day}log.txt"), "a", encoding="utf-8") as log:
                log.write(f"\n{hours}ERROR:{str(e)}")




    def _make_indicators_data(self):
        print("\nStart first operation completed\n")
        codes_actions = self._extract_codes_actions()
        self._list_is_valid(codes_actions)
        os.system("cls")
        print("\nOperation completed\n")
        time.sleep(2)
        print("\nStart second operation completed\n")

        table_data = {}
        count = 0
        for code_action in codes_actions:
            count+=1
            data = self._try_extract(code_action,count)
            table_data = table_data | data
            time.sleep(self._delay)
                        
        df = pd.DataFrame(table_data)
        df.to_csv(self._csv_path("actions_indicators.csv"))
        os.system("cls")
        print("\nScraping finished\n")


    def _try_extract(self,code_action,count):
        try:
            data = self._extract_indicators(code_action)
            print(f"{count}° - operation completed - {code_action}")
            return data
                  
        except Exception as e:
            day = datetime.now().strftime("%Y-%m-%d")
            hours = datetime.now().strftime("%H:%M:%S")            
            with open(self._log_path(f"{day}log.txt"), "a", encoding="utf-8") as log:
                log.write(f"\n{hours} - {code_action} - [Extraction] ERROR:{str(e)}")
                print(f"{count}° - operation failure - {code_action}")
            return {}
        



    def _extract_indicators(self,code_action):
        url = f"http://www.infomoney.com.br/{code_action}"
        response = requests.get(url,headers=self._headers)
        soup  = BeautifulSoup(response.text, "html.parser")
        table = soup.find_all("div",class_="tables")
        data = [td.get_text(strip=True) for td in table[1].find_all("td")]
        data_dict = dict(zip(data[::2], data[1::2]))
        data_dict.update({"Code action":code_action})
        return data_dict



    def _extract_codes_actions(self):
        data = self._get_data()       
        df_dados = pd.DataFrame(data)
        codes_actions = df_dados["StockCode"].to_list()
        return codes_actions
    

    def _get_data(self):
        page = 1   
        data = []
        while True: 
            url = f"https://api.infomoney.com.br/ativos/top-alta-baixa-por-ativo/acao?sector=Todos&orderAtributte=Volume&pageIndex={page}&pageSize=15&search="
            resp = requests.get(url,headers=self._headers)
            if resp.status_code != 200 or not resp.json():
                break
            monitor = resp.json()["Data"]
            print(f"Pagina: {page} - \n{[stockcode["StockCode"] for stockcode in monitor]}")
            if len(monitor) == 0:
                break
            data.extend(resp.json()["Data"])           
            page += 1
            time.sleep(self._delay)
        
        return data
    


    def _list_is_valid(self,data):
        if len(data) == 0 or data is None:
            print("operation failure")
            raise NoData()
        




    def _log_path(self,name):
        base_dir = os.path.dirname(os.path.abspath(__file__))      
        log_dir = os.path.join(base_dir, 'logs')        
        os.makedirs(log_dir, exist_ok=True)        
        log_file = os.path.join(log_dir, name)
        return log_file
    
    def _csv_path(self,name):
        base_dir = os.path.dirname(os.path.abspath(__file__))      
        log_dir = os.path.join(base_dir, 'extraction')        
        os.makedirs(log_dir, exist_ok=True)        
        log_file = os.path.join(log_dir, name)
        return log_file





