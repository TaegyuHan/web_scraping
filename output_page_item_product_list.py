from bs4 import BeautifulSoup


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
        html_list_result.append("인기도(1개월)")

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
