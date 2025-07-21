import requests
import pandas as pd
import time
import numpy as np


dados = []

def get_data():
    global dados
    page = 1
    delay = np.random.uniform(1,2)
    monitor = 0
    headers = {
        "Accept-Language": "pt-BR",
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    while True: 
        _url = f"https://api.infomoney.com.br/ativos/top-alta-baixa-por-ativo/acao?sector=Todos&orderAtributte=Volume&pageIndex={page}&pageSize=15&search="
        resp = requests.get(_url,headers=headers)

        if resp.status_code != 200 or not resp.json():
            break
        
        dados.extend(resp.json()["Data"])
        
        print(f"Pagina: {page}, {dados[monitor].get("StockCode", "Código não encontrado")}")
        page += 1
        monitor +=15
        time.sleep(delay)
    

try:
    get_data()
except Exception as e:
    print(e)

df = pd.DataFrame(dados)

df.to_csv("Actions.csv")



