import requests
from bs4 import BeautifulSoup

filePath = open("C:/Users/Vic/Desktop/Uni Tri 2 2021/Economic Policy Analysis 3312AFE/Group Assignment/RBA Bulletin feeds")

# url = "https://www.rba.gov.au/publications/bulletin/"
# webPage = requests.get(url)

soup = BeautifulSoup(filePath, 'html.parser')

soup.prettify()

print(list(soup.children))
