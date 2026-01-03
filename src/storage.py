import csv
import os


def save_to_csv(movies, filename="data/douban_top250.csv"):
    # 确保 data 目录存在
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "rating", "comments", "year"]
        )
        writer.writeheader()
        writer.writerows(movies)

    print(f"已保存 {len(movies)} 条数据到 {filename}")
