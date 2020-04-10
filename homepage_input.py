import requests
import csv
from bs4 import BeautifulSoup
from output_page_number import make_page_nunber
from output_page_item_link import make_link
from output_page_item_product_list import make_product_information
from output_page_item_product_contents_list import make_product_information_result
from output_dict import make_dictionary
from output_make_dict import make_dictionary_original
from input_csv import input_csv

csv.register_dialect("hashes", delimiter="#")
file = open("2020_02_02.csv", mode="w", encoding="utf-8", newline="")
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
file.close()

item_dict = {
    "top": "001",
    "outer": "002",
    "onepiece": "020",
    "pants": "003",
    "skirt": "022",
    "bag": "004",
    "sneaker": "018",
    "shoes": "005",
    "watch": "006",
    "headwear": "007",
    "sports/goods": "017",
    "leg/underwear": "008",
    "eyewear": "009",
    "accessory": "011",
    "digital/tech": "012",
    "life": "013",
    "beauty": "015",
    "pet": "021",
    "culture": "014",
}


def make_item_page():
    for item_number in item_dict.values():
        print("make_item_number")
        page = "1"
        html = requests.get(
            f"https://store.musinsa.com/app/items/lists/{item_number}/?category=&d_cat_cd={item_number}&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=80&page={page}&page_kind=category&list_kind=small&free_dlv=&ex_soldout=&sale_goods=&exclusive_yn=&price=&color=&a_cat_cd=&sex=&size=&tag=&popup=&brand_favorite_yn=&goods_favorite_yn=&blf_yn=&price1=&price2=&brand_favorite=&goods_favorite=&chk_exclusive=&chk_sale=&chk_soldout="
        )
        total_pageing_num = int(make_page_nunber(html))
        print(total_pageing_num)
        for page_num in range(1, total_pageing_num + 1):
            print("make_link")
            html = requests.get(
                f"https://store.musinsa.com/app/items/lists/{item_number}/?category=&d_cat_cd={item_number}&u_cat_cd=&brand=&sort=pop&sub_sort=&display_cnt=80&page={page_num}&page_kind=category&list_kind=small&free_dlv=&ex_soldout=&sale_goods=&exclusive_yn=&price=&color=&a_cat_cd=&sex=&size=&tag=&popup=&brand_favorite_yn=&goods_favorite_yn=&blf_yn=&price1=&price2=&brand_favorite=&goods_favorite=&chk_exclusive=&chk_sale=&chk_soldout="
            )
            link_list = make_link(html)
            for link in link_list:
                html_link = f"https://store.musinsa.com{link}"
                print(html_link)
                html = requests.get(f"https://store.musinsa.com{link}")
                html_product_list = make_product_information(html)
                html_product_contents_list = make_product_information_result(
                    html, html_product_list, html_link
                )
                html_product_dict = make_dictionary(
                    html_product_list, html_product_contents_list
                )
                make_dictionary_final = make_dictionary_original(html_product_dict)
                input_csv(make_dictionary_final)


a = make_item_page()
print("finish")