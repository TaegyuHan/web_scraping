import csv


def input_csv(html):
    file = open("2020_02_02.csv", mode="a", encoding="utf-8", newline="")
    writer = csv.writer(file, dialect="hashes")
    writer.writerow(list(html.values()))
    file.close()
