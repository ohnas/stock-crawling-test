import time
import requests
from bs4 import BeautifulSoup
from tools import get_yesterday
from sheets import append_values, append_logs

stocks = [
    {
        "name": "VANGUARD S&P 500 ETF",
        "code": "VOO",
        "url": "https://kr.investing.com/etfs/vanguard-s-p-500",
    },
    {
        "name": "테슬라",
        "code": "TSLA",
        "url": "https://kr.investing.com/equities/tesla-motors",
    },
    {
        "name": "마이크로스포트",
        "code": "MSFT",
        "url": "https://kr.investing.com/equities/microsoft-corp",
    },
    {
        "name": "코스트코 홀세일",
        "code": "COST",
        "url": "https://kr.investing.com/equities/costco-whsl-corp-new",
    },
    {
        "name": "엔비디아",
        "code": "NVDA",
        "url": "https://kr.investing.com/equities/nvidia-corp",
    },
    {
        "name": "메타 플랫폼스(페이스북)",
        "code": "META",
        "url": "https://kr.investing.com/equities/facebook-inc",
    },
    {
        "name": "애플",
        "code": "AAPL",
        "url": "https://kr.investing.com/equities/apple-computer-inc",
    },
    {
        "name": "알파벳 A",
        "code": "GOOGL",
        "url": "https://kr.investing.com/equities/google-inc",
    },
    {
        "name": "아마존닷컴",
        "code": "AMZN",
        "url": "https://kr.investing.com/equities/amazon-com-inc",
    },
    {
        "name": "팔란티어 테크",
        "code": "PLTR",
        "url": "https://kr.investing.com/equities/palantir-technologies-inc",
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

YESTERDAY = get_yesterday()

for stock in stocks:
    try:
        response = requests.get(url=stock["url"], headers=HEADERS)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find("div", {"data-test": "instrument-price-last"})
        previous_close = div.text
        values = [
            [stock["name"], stock["code"], YESTERDAY, previous_close, "나스닥", "USD"]
        ]
        append_values(values)
        append_logs(YESTERDAY, "success", "-", "crawling", stock["code"])
    except requests.exceptions.HTTPError as http_err:
        append_logs(YESTERDAY, "fail", http_err, "HTTPError", stock["code"])
    except requests.exceptions.RequestException as req_err:
        append_logs(YESTERDAY, "fail", req_err, "ReQuestException", stock["code"])
    except Exception as err:
        append_logs(YESTERDAY, "fail", err, "Exception", stock["code"])
    finally:
        time.sleep(1)
