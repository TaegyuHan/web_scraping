from bs4 import BeautifulSoup


def make_link(html):
    html = BeautifulSoup(html.text, "html.parser")
    link_list = []
    html_list = html.find_all("div", class_="list_img")
    for link in html_list:
        link_list.append(link.find("a").get("href"))
    return link_list

