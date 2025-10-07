import sys
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
        self._base_dir = ""

    def run(self):

        print("\nStart first operation completed\n")
        codes_actions = self._extract_codes_actions()
        self._list_is_valid(codes_actions)
        os.system("cls")        
        print("\nOperation completed\n")
        time.sleep(3)

        os.system("cls")
        print("\nStart second operation completed\n")
        self._try_make_indicators_data(codes_actions)
        

    def _try_make_indicators_data(self,codes_actions):
        try:
            self._make_indicators_data(codes_actions)
        except Exception as e:
            day = datetime.now().strftime("%Y-%m-%d")
            hours = datetime.now().strftime("%H:%M:%S")            
            with open(self._path(f"./{day}log.txt","logs"), "a", encoding="utf-8") as log:
                log.write(f"\n{hours}ERROR:{str(e)}")
                print("Sorry something went wrong :/")


    def _make_indicators_data(self,codes_actions):
        table_data = []
        count = 0
        for code_action in codes_actions:
            count+=1
            data = self._try_extract_indicators_of(code_action,count)
            table_data.append(data)
            time.sleep(self._delay)
                    
        df = pd.DataFrame(table_data)
        df.to_csv(self._path("./actions_indicators.csv","extraction"))
        os.system("cls" if os.name == "nt" else "clear") 
        print("\nScraping finished\n")


    def _try_extract_indicators_of(self,code_action,count):
        try:
            data = self._extract_indicators_of(code_action)
            print(f"{count}° - operation completed - {code_action}")
            return data
                  
        except Exception as e:
            day = datetime.now().strftime("%Y-%m-%d")
            hours = datetime.now().strftime("%H:%M:%S")            
            with open(self._path(f"./{day}log.txt","logs"), "a", encoding="utf-8") as log:
                log.write(f"\n{hours} - {code_action} - [Extraction] ERROR:{str(e)}")
                print(f"{count}° - operation failure - {code_action}")
            return {}
        



    def _extract_indicators_of(self,code_action):
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
        




    def _path(self, name, dir):
        if getattr(sys, "frozen", False):
            self._base_path = os.path.dirname(sys.executable)
        else:
            self._base_path = os.path.dirname(os.path.abspath(__file__))

        path_final = os.path.join(self._base_path, dir)
        os.makedirs(path_final, exist_ok=True)
        return os.path.join(path_final, name)
    
  


