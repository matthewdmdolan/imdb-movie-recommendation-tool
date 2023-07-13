from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from bs4 import BeautifulSoup as bs
import lxml.html as lh
from lxml.html import builder as E
import re


"""AT THE MOMENT THIS IS A TEST WITH JUST ONE FILM TO SEE WHAT WE CAN SCRAPE FROM HERE"""

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