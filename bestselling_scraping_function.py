import requests
import pandas as pd
import os
from bs4 import BeautifulSoup

'''
This function will:
1. Get the list of categories from the bestseller homepage
2. Get the list of top 15 books from each category, and also the information about each book
3. Create a neatly organized CSV file of the books found
'''

# Will return a list of categories for bestsellers
def get_category_titles(doc):
    # Trying to find the categories - methodology is by specifying the HTML class in which the category is located
    category_title_tags = doc.find_all('a', {'class': 'css-nzgijy'})
    # Creating a list of category titles
    # To get just the text use .text
    category_titles = []
    for tag in category_title_tags:
        category_titles.append(tag.text)
    return category_titles


# Will return a list of urls for the respective categories
def get_category_urls(doc):
    # Finding URL for the categories - same as before, see the issue I ran into above
    category_link_tags = doc.find_all('a', {'class': 'css-nzgijy'})
    # Creating a list of category urls
    # To get just the text use .text
    category_links = []
    base_url = "https://www.nytimes.com"
    for tag in category_link_tags:
        category_links.append(base_url + tag['href'])
    return category_links


# This function will scrape the NYT bestsellers website for the categories, and the individual URLs
def scrape_bestselling_categories():
    # Original NYT Bestsellers link
    bestsellers_url = 'https://www.nytimes.com/books/best-sellers/'

    # See bestsellers-download.py for explanation on requests library
    response = requests.get(bestsellers_url)
    # Will notify if the request failed
    if response.status_code != 200:
        raise Exception('Failed to lad page {}'.format(bestsellers_url))

    # beautiful soup parses the website
    doc = BeautifulSoup(response.text, 'html.parser')

    categories_dict = {
        'Category': get_category_titles(doc),
        'Category URL': get_category_urls(doc)
    }

    return pd.DataFrame(categories_dict)


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

    # Function to return all the information about a book
    def get_book_info(title_tag, author_tag, desc_tag, time_tag, publisher_tag):
        book_title = title_tag.text
        author = author_tag.text.strip("by ")
        time = time_tag.text
        description = desc_tag.text
        publisher = publisher_tag.text
        return book_title, author, time, description, publisher

    for i in range(len(title_tags)):
        info = get_book_info(title_tags[i], author_tags[i], desc_tags[i], time_tags[i], publisher_tags[i])
        book_dict['Book Title'].append(info[0])
        book_dict['Author'].append(info[1])
        book_dict['Publisher'].append(info[4])
        book_dict['Description'].append(info[3])
        book_dict['Time on Bestseller List'].append(info[2])

    # Pandas creates a nice looking dataframe to organize the data
    return pd.DataFrame(book_dict)


# Function to download information on the category - based on the url chosen
def get_category_page(category_url):
    response = requests.get(category_url)
    if response.status_code != 200:
        raise Exception('Failed to lad page {}'.format(category_url))
    category_doc = BeautifulSoup(response.text, 'html.parser')
    return category_doc


# Function to scrape an individual category's books
def scrape_category_books(category_url, path):
    # Pay attention to the order of the functions
    category_df = get_category_books(get_category_page(category_url))

    # Checking if the file already exists
    if os.path.exists(path):
        print("The file {} already exists. Skipping...".format(path))
        return

    # Saving all of the information into a csv file
    category_df.to_csv(path, index=None)


def scrape_all_bestselling():
    categories_df = scrape_bestselling_categories()
    # Iterrate through the rows in a Pandas dataframe

    # Makeing a directory for the .csv files
    os.makedirs('bestsellers-data', exist_ok=True)

    for index, row in categories_df.iterrows():
        print('Scraping top books for "{}"'.format(row['Category']))
        scrape_category_books(row['Category URL'], 'bestsellers-data/{}.csv'.format(row['Category']))


# Calling the function
scrape_all_bestselling()
