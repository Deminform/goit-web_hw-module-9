import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# first_paragraph = soup.find('p')
# first_paragraph_text = first_paragraph.get_text()
# print(first_paragraph.text.strip())

# all_paragraph = soup.find_all('p')
# for el in all_paragraph:
#     print(el.get_text)

# first_link = soup.find('a')
# print(first_link['href'])

# body_children = list(first_paragraph.children)
# print(body_children)

# first_div = soup.find('div')
# first_div_link = first_div.find('a')
# print(first_div_link)

# first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)

# container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
# print(container)

next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
# print(next_sibling)

previous_sibling = next_sibling.find_previous_sibling("span")
print(previous_sibling)

