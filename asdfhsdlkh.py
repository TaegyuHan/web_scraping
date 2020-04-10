csv.register_dialect("hashes", delimiter="#")
file = open("item.csv", mode="w", encoding="utf-8")
writer = csv.writer(file, dialect="hashes")
writer.writerow(
    [
        "품명|영어",
        "범주",
        "브랜드/품번",
        "인기도(1개월_장바구니)",
        "누적판매",
        "좋아요",
        "구매후기",
        "배송방법",
        "평균배송일",
        "판매가",
        "세일가",
        "링크",
    ]
)
