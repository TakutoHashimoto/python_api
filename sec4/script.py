import requests
import os
import pandas as pd


URL = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
API_KEY = os.environ.get("API_KEY")

params = {
    "key": API_KEY,
    "keyword": "沖縄",
    "count": 100,
    "format": "json"
}

res = requests.get(URL, params)
print(res.status_code)

result = res.json()
items = result["results"]["shop"]
print(len(items))


df = pd.DataFrame(items)
print(df.shape)
print(df.head())

print(df.columns)
df = df[["name", "address", "wifi"]]
print(df.head())

df.to_csv("hotpepper.csv", index=False)