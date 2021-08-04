import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to download information on the category - based on the url chosen
def get_category_page(category_url):
    response = requests.get(category_url)
    if response.status_code != 200:
        raise Exception('Failed to lad page {}'.format(category_url))
    category_doc = BeautifulSoup(response.text, 'html.parser')
    return category_doc

# Function to return all the information about a book
def get_book_info(title_tag, author_tag, desc_tag, time_tag, publisher_tag):
    book_title = title_tag.text
    author = author_tag.text.strip("by ")
    time = time_tag.text
    description = desc_tag.text
    publisher = publisher_tag.text
    return book_title, author, time, description, publisher

# Function to, based on the category, give the information on the books under that category
def get_category_books(category_doc):
    # Getting the information necessary
    title_tags = category_doc.find_all('h3', {'class': 'css-5pe77f'})
    author_tags = category_doc.find_all('p', {'class': 'css-hjukut'})
    publisher_tags = category_doc.find_all('p', {'class': 'css-heg334'})
    desc_tags = category_doc.find_all('p', {'class': 'css-14lubdp'})
    time_tags = category_doc.find_all('p', {'class': 'css-1o26r9v'})

    # Saving the category level information as a dictionary, so it is easily formatted into a dataframe
    book_dict = {
        "Book Title": [],
        "Author": [],
        "Publisher": [],
        "Description": [],
        "Time on Bestseller List": []
    }

    for i in range(len(title_tags)):
        info = get_book_info(title_tags[i], author_tags[i], desc_tags[i], time_tags[i], publisher_tags[i])
        book_dict['Book Title'].append(info[0])
        book_dict['Author'].append(info[1])
        book_dict['Publisher'].append(info[4])
        book_dict['Description'].append(info[3])
        book_dict['Time on Bestseller List'].append(info[2])

    # Pandas creates a nice looking dataframe to organize the data
    return pd.DataFrame(book_dict)


f_link = open('./bestseller-categories/category_links.txt')
f_link = f_link.readlines()

category_links = []

for url in f_link:
    category_links.append(url.strip('\n'))

url4 = category_links[3]

category4_doc = get_category_page(url4)

category4_books = get_category_books(category4_doc)

print(category4_books)