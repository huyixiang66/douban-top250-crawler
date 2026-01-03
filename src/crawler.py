import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://movie.douban.com/",
    "Connection": "keep-alive",
}

def fetch_top250_page(start=0):
    url = "https://movie.douban.com/top250"
    params = {"start": start}
    resp = requests.get(
        url,
        headers=HEADERS,
        params=params,
        timeout=10
    )
    resp.raise_for_status()
    return resp.text


