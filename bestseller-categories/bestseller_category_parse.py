from bs4 import BeautifulSoup

page_contents = open('./bestsellers.html', 'r')

# beautiful soup parses the website
doc = BeautifulSoup(page_contents, 'html.parser')

# Trying to find the categories - methodology is by specifying the HTML class in which the category is located
# Note I was finding an <a> tag, if I was searching for a <div> or an <h2> or whatever, I would have to specify that
# Unfortunatey the NYT website was set up in such a way that I could not find a div which had the heading
# Also, note that I had to specify I was searching for
category_title_tags = doc.find_all('a', {'class': 'css-nzgijy'})

# Creating a list of category titles
# To get just the text use .text
category_titles = []
for tag in category_title_tags:
    category_titles.append(tag.text)

# Finding URL for the categories - same as before, see the issue I ran into above
category_link_tags = doc.find_all('a', {'class': 'css-nzgijy'})

# Creating a list of category urls
category_links = []
base_url = "https://www.nytimes.com"
for tag in category_link_tags:
    category_links.append(base_url + tag['href'])

fout = open('bestseller-categories/category_headers.txt', 'w')
for ele in category_titles:
    fout.write(ele + '\n')
fout.close()

fout = open('bestseller-categories/category_links.txt', 'w')
for ele in category_links:
    fout.write(ele + '\n')
fout.close()
