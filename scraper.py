import requests
from bs4 import BeautifulSoup
from columnar import columnar
import numpy as np
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

title = []
company = []
location = []

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    formatted_title_element = title_element.text.strip()
    formatted_company_element = company_element.text.strip()
    formatted_location_element = location_element.text.strip()

    title.append(formatted_title_element)
    company.append(formatted_company_element)
    location.append(formatted_location_element)

# data = []
# data.append(title)
# data.append(company)
# data.append(location)

# headers = ['Title', 'Company', 'Location']
# table = columnar(data, headers, no_borders=True, head=50)
# print(table)

data = [[title],[company],[location]]
df1 = pd.DataFrame(data)

print(type(data))

l = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]
df2 = pd.DataFrame(l)

print(type(l))

print(df1)
#print(df2)

