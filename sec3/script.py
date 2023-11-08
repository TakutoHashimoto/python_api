import requests


url = "https://jsonplaceholder.typicode.com/posts/"
res = requests.get(url)
print(f"status code: {res.status_code}")

print(res.json()[:5])

datum = res.json()[0]
print(datum["title"])

print("==========")

body = {
    "id": 5
}

res_2 = requests.get(url, body)
print(res_2.json())
