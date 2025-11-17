import requests as r

url: str = "https://api.quotable.io/random"

request: r.Request = r.get(url=url)
data: dict = request.json()

# print(data)
print("Quote:", data.setdefault("content", None))
print("Author:", data.setdefault("author", None))
