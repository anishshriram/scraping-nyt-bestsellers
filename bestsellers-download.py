import requests

bestsellers_url = 'https://www.nytimes.com/books/best-sellers/'

# requests will go to the bestsellers website, and then download it as a response object
response = requests.get(bestsellers_url)

'''
To check if requests actually worked
print(response.status_code)
Status code 200 is good (codes between 200-299)
Other HTTP status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


'''

# The entire page is stored here - the html source code
page_contents = response.text

# Storing it as an html file
with open('bestsellers.html', 'w') as f:
    f.write(page_contents)

print(len(response.text))

