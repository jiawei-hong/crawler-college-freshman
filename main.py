from bs4 import BeautifulSoup
import requests


BASE_URL = 'https://university-tw.ldkrsi.men/register/'

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, 'html.parser')
unready_university_rate = []

for tr in soup.find('section', {"class": "four"}).table.tbody.find_all('tr'):
    td_element = tr.find_all('td')
    [university_name, university_register_rate] = [
        td_element[0].find('a').text, td_element[1].text]
    unready_university_rate.append([
        university_name, float(university_register_rate.replace('%', ''))])

with open('university_freshman_register_rate.csv', 'w', encoding="utf-8") as f:
    for [name, rate] in sorted(unready_university_rate, key=lambda x: x[1], reverse=True):
        f.write(f'{name},{str(rate)}%\n')
