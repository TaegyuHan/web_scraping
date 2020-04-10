import csv

html = {
    "품명|영어": "레이아웃 어센틱 로고 롱슬리브 레몬|레이아웃 어센틱 로고 롱슬리브 레몬",
    "범주": "상의> 긴팔 티셔츠(커버낫)",
    "브랜드/품번": "COVERNAT / C2001LT10LM",
    "시즌/성별": " 2020  S/S/남",
    "인기도(1개월_장바구니)": "148",
    "좋아요": "100",
    "배송방법": "국내 배송 /  입점사 배송 ",
    "평균배송일": "3.1일 / 롯데택배 (영업일 기준, 결제 후 평균 배송기간)",
    "판매가": "45,000",
    "링크": "https://store.musinsa.com/app/product/detail/1284678/0",
}

csv.register_dialect("hashes", delimiter="#")


def input_csv(html):
    file = open("item.csv", mode="a", encoding="utf-8", newline="")
    writer = csv.writer(file, dialect="hashes")
    writer.writerow(list(html.values()))
    file.close()


input_csv(html)
