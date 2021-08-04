from individual_category_parse import *
import pandas as pd

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
book_info_DataFrame = pd.DataFrame(book_dict)

# Creating a CSV file with the extracted information
book_info_DataFrame.to_csv('../individual-categories/individual_information.csv', index=None)