import re
from bs4 import BeautifulSoup


def make_page_nunber(html):
    html = BeautifulSoup(html.text, "html.parser")
    html = html.find("span", class_="totalPagingNum")
    numbers = re.findall("\d+", html.text)
    return numbers[0]
