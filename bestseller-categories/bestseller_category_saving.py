import pandas as pd

f_head = open('bestseller-categories/category_headers.txt')
f_head = f_head.readlines()

f_link = open('bestseller-categories/category_links.txt')
f_link = f_link.readlines()

category_headers = []
category_links = []

for header in f_head:
    category_headers.append(header.strip('\n'))

for url in f_link:
    category_links.append(url.strip('\n'))


# Saving the category level information as a dictionary, so it is easily formated into a dataframe
category_dict = {
    'Header': category_headers,
    'Hyperlink': category_links
}

# Pandas creates a nice looking dataframe to organize the data
category_DataFrame = pd.DataFrame(category_dict)

# Creating a CSV file with the extracted information
category_DataFrame.to_csv('bestseller-categories/category_information.csv', index=None)

