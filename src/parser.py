from bs4 import BeautifulSoup


def parse_movies(html: str):
    soup = BeautifulSoup(html, "html.parser")

    items = soup.find_all("div", class_="item")
    movies = []

    for item in items:
        # 1. 电影名
        title = item.find("span", class_="title").get_text(strip=True)

        # 2. 评分
        rating = item.find("span", class_="rating_num").get_text(strip=True)

        # 3. 评价人数
        comment_text = item.find_all("span")[-1].get_text(strip=True)
        # 例如： "123456人评价"
        comment_count = comment_text.replace("人评价", "")

        # 4. 年份（粗略提取）
        info = item.find("div", class_="bd").p.get_text()
        year = info.strip().split("\n")[1].strip()[:4]

        movies.append({
            "title": title,
            "rating": rating,
            "comments": comment_count,
            "year": year
        })

    return movies
