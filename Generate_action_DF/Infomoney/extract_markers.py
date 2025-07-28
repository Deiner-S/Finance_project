import requests
from bs4 import BeautifulSoup

header = {
            "Accept-Language": "pt-BR",
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        } 
url = "https://www.infomoney.com.br/cotacoes/b3/acao/petrobras-petr4/"
response = requests.get(url,headers=header)
soap = BeautifulSoup(response.text, "html.parser")
marker = soap.find("div",class_="tables")

marker = str(marker)
marker = marker.replace("<tr>", "")
marker = marker.replace("</tr>", ",")
marker = marker.replace("</td>", ":")

replacementes = {"<table>":"",
                         "</table>":"",
                         """</div>""":"",
                         """<div class="tables">""":"",
                         """<td class="negative">""":"",
                         "<tr>":"",
                         """<td class="positive">""":"",
                         "<td>":""
                         }
for antigo, novo in replacementes.items():
    marker = marker.replace(antigo,novo)
marker = marker.replace("\n", "").replace("\r", "").replace("\xa0", "").strip()

# Ver resultado
print("🧼 Texto limpo:\n", marker)

# Separação
markerlist = marker.split(",")
print("\n🔍 Lista final:")
for item in markerlist:
    print(item)