# Scraping Bestselling Books on the NYT Bestselling List

TODO:

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.

The New York Times puts out a bestsellers list of books doing well. It can be helpful to get some information from the site to get good books to read.

There were a couple tools I used to complete this project. I used the computer programming language Python for the bulk of the code. Experience with HTML
and CSS were particularly useful in grabbing the class names to specify my searches when parsing.

I also used a couple Python packages and libraries. Requests (to send HTTP requests extremely easily), Beautiful Soup (to parse HTML documents), Pandas (to develop easy
to read and understand data structures), and OS (which offers functionality to interact with my operating system)

Outline of the Project
  - used requests to download the page
  - used BS4 to parse and extract information
  - converted into a pandas dataframe
  - converted into a CSV file

1. Scraped https://www.nytimes.com/books/best-sellers/
2. Compiled a list of categories provided, such as Hardcover Nonfiction, Advice, How To, etc
3. From each category, the top 15 books were selected, and information including the title, author, publisher, and its time on the list was grabbed
4. The information was put into a Pandas DataFrame and then transfered into CSV files

All functions created were commented thoroughly for ease of understanding

Resources Used:

- Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Requests Documentation: https://docs.python-requests.org/en/master/
- Reading Relative File Paths in Python: https://www.youtube.com/watch?v=B3M1bQD1Xyk&pp=sAQA
