import requests
from bs4 import BeautifulSoup

URL = "https://kr.investing.com/etfs/vanguard-s-p-500"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

response = requests.get(url=URL, headers=HEADERS)
status = response.status_code
print(status)
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", {"data-test": "instrument-price-last"})

print(div.text)
