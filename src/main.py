from crawler import fetch_top250_page
from parser import parse_movies
from storage import save_to_csv
import time


def main():
    all_movies = []

    for start in range(0, 250, 25):
        print(f"正在爬取 start={start}")

        try:
            html = fetch_top250_page(start)
        except Exception as e:
            print("请求失败：", e)
            print("跳过本页")
            continue

        movies = parse_movies(html)
        print(f"本页解析到 {len(movies)} 条")

        all_movies.extend(movies)

        time.sleep(5)   # ⭐ 非常重要，别删

    print(f"总共获取 {len(all_movies)} 条电影")

    save_to_csv(all_movies)


if __name__ == "__main__":
    main()
