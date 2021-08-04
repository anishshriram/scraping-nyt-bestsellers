import requests
from bs4 import BeautifulSoup

f_link = open('../bestseller-categories/category_links.txt', 'r')
f_link = f_link.readlines()

category_links = []
for url in f_link:
    category_links.append(url.strip('\n'))

response = requests.get(category_links[0])

category_doc = BeautifulSoup(response.text, 'html.parser')

# Getting the information necessary
title_tags = category_doc.find_all('h3', {'class': 'css-5pe77f'})
author_tags = category_doc.find_all('p', {'class': 'css-hjukut'})
publisher_tags = category_doc.find_all('p', {'class': 'css-heg334'})
desc_tags = category_doc.find_all('p', {'class': 'css-14lubdp'})
time_tags = category_doc.find_all('p', {'class': 'css-1o26r9v'})


# Function to return all the information about a book
def get_book_info(title_tag, author_tag, desc_tag, time_tag, publisher_tag):
    book_title = title_tag.text
    author = author_tag.text.strip("by ")
    time = time_tag.text
    description = desc_tag.text
    publisher = publisher_tag.text
    return book_title, author, time, description, publisher


