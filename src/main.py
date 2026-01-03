from crawler import fetch_html

if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    html = fetch_html(url)

    print(html[:500])  # 只打印前 500 个字符

