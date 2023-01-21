from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://university-tw.ldkrsi.men/register/'

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, 'html.parser')
unready_university_rate = []

university_categories = ['公立一般大學', '私立一般大學', '公立技專校院', '私立技專校院']
university_categories_section_classname = ['one', 'three', 'two', 'four']
user_search_university_text = f'請輸入要查詢的學校類別 {" ".join([f"{i+1}. {university_categories[i]}" for i in range(len(university_categories))])}\n'
university_search_input = input(user_search_university_text)

for tr in soup.find('section', {"class": university_categories_section_classname[int(university_search_input) - 1]}).table.tbody.find_all('tr'):
    td_element = tr.find_all('td')
    [university_name, university_register_rate] = [
        td_element[0].find('a').text, td_element[1].text]
    unready_university_rate.append([
        university_name, float(university_register_rate.replace('%', ''))])

with open('university_freshman_register_rate.csv', 'w', encoding="utf-8") as f:
    for [name, rate] in sorted(unready_university_rate, key=lambda x: x[1], reverse=True):
        f.write(f'{name},{str(rate)}%\n')
