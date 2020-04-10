from bs4 import BeautifulSoup


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
        if product == "인기도(1개월)":
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
                .text
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
