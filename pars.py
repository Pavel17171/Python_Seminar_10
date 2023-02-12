import requests
from bs4 import BeautifulSoup

def dollar():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[3].text
    return price
def dollar_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[4].text
    return price


def Australian_dollar():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[13].text
    return price
def Australian_dollar_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[14].text
    return price

def Canadian_dollar():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[73].text
    return price
def Canadian_dollar_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[74].text
    return price


def euro():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[8].text
    return price
def euro_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[9].text
    return price

def GBP():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[143].text
    return price
def GBP_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[144].text
    return price

def belarussian_ruble():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[28].text
    return price
def belarussian_ruble_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[29].text
    return price



def yuan():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[83].text
    return price
def yuan_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[84].text
    return price

def yen():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[168].text
    return price
def yen_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[169].text
    return price

def Singapore_dollar():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[118].text
    return price
def Singapore_dollar_change():
    link = 'https://www.banki.ru/products/currency/cb/'
    responce = requests. get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    table = soup.find('table', class_='standard-table standard-table--row-highlight')
    price = table.find_all('td')[119].text
    return price