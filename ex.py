import requests
import csv
from bs4 import BeautifulSoup

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
file.close()


def make_product_information(html):
    html = BeautifulSoup(html.text, "html.parser")
    html_list = []
    html_item_list = []
    html_item_str_list = []
    html_list.append(
        html.find("div", class_="explan_product product_info_section").find_all(
            "p", class_="product_article_tit"
        )
    )

    html_list.append(
        html.find("div", class_="explan_product delivery_info_section").find_all(
            "p", class_="product_article_tit"
        )
    )
    html_list.append(
        html.find("div", class_="explan_product price_info_section").find_all(
            "p", class_="product_article_tit"
        )
    )

    for x in html_list:
        for i in x:
            html_item_list.append(i.text)

    for x in html_item_list:
        html_item_str_list.append(x.replace("\n", "").replace("\t", ""))
    return make_product_information_list(html_item_str_list)


def make_product_information_list(html_list):
    html_list_result = []
    html_str = "".join(html_list)
    html_list_result.append("품명|영어")
    html_list_result.append("범주")
    if html_str.find("브랜드") != -1:
        html_list_result.append("브랜드/품번")

    if html_str.find("시즌") != -1:
        html_list_result.append("시즌/성별")

    if html_str.find("인기도") != -1:
        html_list_result.append("인기도(1개월_장바구니)")

    if html_str.find("누적판매") != -1:
        html_list_result.append("누적판매")

    if html_str.find("좋아요") != -1:
        html_list_result.append("좋아요")

    if html_str.find("구매 후기") != -1:
        html_list_result.append("구매후기")

    if html_str.find("배송 방법") != -1:
        html_list_result.append("배송방법")

    if html_str.find("평균 배송일") != -1:
        html_list_result.append("평균배송일")

    if html_str.find("무신사 판매가") != -1:
        html_list_result.append("판매가")

    if html_str.find("무신사 세일가") != -1:
        html_list_result.append("세일가")
    html_list_result.append("링크")
    return html_list_result


link = "https://store.musinsa.com/app/product/detail/1284678/0"
r = requests.get("https://store.musinsa.com/app/product/detail/1284678/0")
b = make_product_information(r)


def make_product_information_result(html, make_product_information_list, html_link):
    html = BeautifulSoup(html.text, "html.parser")
    make_product_information_list = make_product_information_list
    make_product_information_contents_list = []
    for product in make_product_information_list:
        if product == "품명|영어":
            make_product_information_contents_list.append(
                html.find("div", class_="right_contents section_product_summary")
                .find("span", class_="product_title")
                .text.replace("\n", "")
                .replace("\t", "")
            )
        if product == "범주":
            make_product_information_contents_list.append(
                html.find("div", class_="right_contents section_product_summary")
                .find("p", class_="item_categories")
                .text.replace("\n", "")
                .replace("\t", "")
            )
        if product == "브랜드/품번":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product product_info_section")
                .find("p", class_="product_article_contents")
                .text
            )
        if product == "시즌/성별":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product product_info_section")
                .find("span", class_="txt_gender")
                .parent.text.replace("\n", "")
                .replace("\t", "")
            )
        if product == "인기도(1개월_장바구니)":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product product_info_section")
                .find("span", class_="wish_number")
                .previous_element
            )
        if product == "누적판매":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product product_info_section")
                .find("strong", id="sales_1y_qty")
                .text
            )
        if product == "좋아요":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product product_info_section")
                .find("span", class_="prd_like_cnt")
                .text
            )
        if product == "구매후기":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product product_info_section")
                .find("a", class_="link_type")
                .parent.text.replace("\n", "")
                .replace("\t", "")
            )
        if product == "배송방법":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product delivery_info_section")
                .find("li", class_="box_info_products")
                .find("p", class_="product_article_contents")
                .text
            )
        if product == "평균배송일":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product delivery_info_section")
                .find("ul", class_="product_article")
                .find("p", class_="product_article_contents del")
                .text
            )
        if product == "판매가" and "세일가" in make_product_information_list:
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product price_info_section")
                .find("span", id="goods_price")
                .find("del")
            )
        elif product == "판매가":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product price_info_section")
                .find("span", id="goods_price")
                .text.replace("\n", "")
                .replace("\t", "")
            )
        if product == "세일가":
            make_product_information_contents_list.append(
                html.find("div", class_="explan_product price_info_section")
                .find("span", id="sale_price")
                .text.replace("\n", "")
                .replace("\t", "")
            )
    make_product_information_contents_list.append(html_link)
    return make_product_information_contents_list


c = make_product_information_result(r, b, link)


def make_dictionary(
    make_product_information_list, make_product_information_contents_list
):
    make_product_information_dict = {}
    make_product_information_len = len(make_product_information_list)
    for num in range(make_product_information_len):
        make_product_information_dict[
            make_product_information_list[num]
        ] = make_product_information_contents_list[num]
    return make_product_information_dict


a = make_dictionary(b, c)
print(a)


def make_dictionary_original(make_product_information_dict):
    make_product_information_dict_result = {}
    make_product_information_dict_comparison = [
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
    make_product_information_dict_key_list = list(make_product_information_dict.keys())
    for num in range(len(make_product_information_dict_comparison)):
        if (
            make_product_information_dict_comparison[num]
            in make_product_information_dict_key_list
        ):
            make_product_information_dict_result.update(
                {
                    make_product_information_dict_comparison[
                        num
                    ]: make_product_information_dict[
                        make_product_information_dict_comparison[num]
                    ]
                }
            )
        else:
            make_product_information_dict_result.update(
                {make_product_information_dict_comparison[num]: ""}
            )
    return make_product_information_dict_result


g = make_dictionary_original(a)


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


file = open("item.csv", mode="a", encoding="utf-8")
writer = csv.writer(file, dialect="hashes")
writer.writerow(list(make_product_information_dict_result.keys())

