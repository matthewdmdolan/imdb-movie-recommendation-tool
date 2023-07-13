from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from bs4 import BeautifulSoup as bs
import lxml.html as lh
from lxml.html import builder as E
import re

# Set up the Chrome driver service
driver = webdriver.Chrome()

#starting web app
url = "https://m.imdb.com/chart/top/?ref_=nv_mv_500"

# Setting up selenium package parameters
driver = webdriver.Chrome()
driver.get(url)
# access HTML source code with page_source method
s = driver.page_source
print(s)

"""this section removes the javascript info"""
# the regex pattern to match script tags and their content
pattern = re.compile('<script.*?>.*?</script>', re.DOTALL)
# remove script tags
clean_html = re.sub(pattern, '', s)

#converts to prettyprint html
# #convert the generated HTML to a string
soup = bs(clean_html)                #make BeautifulSoup
pretty_html = soup.prettify()

print(pretty_html)

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(pretty_html)

# assuming clean_html contains your HTML
soup = bs(pretty_html, 'html.parser')

# create empty lists to store the data
titles = []
imdb_ratings = []
years_of_release = []

# find all elements with the class 'media-body media-vertical-align'
elements = soup.find_all(class_='media-body media-vertical-align')

for element in elements:
    # extract and save the title
    title_element = element.find('h4')
    title = title_element.contents[1].strip() if title_element else None
    titles.append(title)

    # extract and save the imdb_rating
    imdb_rating_element = element.find(class_='imdb-rating')
    imdb_rating = imdb_rating_element.get_text(strip=True) if imdb_rating_element else None
    imdb_ratings.append(imdb_rating)

    # extract and save the year_of_release
    year_of_release_element = element.find('h4').find(class_='unbold') if title_element else None
    year_of_release = year_of_release_element.contents[0].strip("()") if year_of_release_element else None
    years_of_release.append(year_of_release)

# print the data to check
for title, imdb_rating, year_of_release in zip(titles, imdb_ratings, years_of_release):
    print(f'Title: {title}, IMDB Rating: {imdb_rating}, Year of Release: {year_of_release}')





