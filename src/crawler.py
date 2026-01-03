import requests
import time
import random

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def fetch_html(url):
    """
    请求指定 URL，返回网页 HTML
    """
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()  # 请求失败会直接抛异常

    # 反爬：随机睡眠，降低访问频率
    time.sleep(random.uniform(1, 2))

    return response.text

