from bs4 import BeautifulSoup
import requests
import csv
url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2005"

def world_pop_2005(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table = soup.findAll("table")[1]
    rows = table.find_all('tr')[1:]
    th_td_list = []
    for row in rows[1:-1]:
        th = row.findAll('th')
        tds = row.findAll('td')[:-1]
        th_td_data_row = []
        for td in tds:
            td_text = td.text.strip()            
            th_td_data_row.append(td_text)              
        th_td_list.append(th_td_data_row)
    return th_td_list

def data_to_csv(url):
    with open("clariza_mayo_population.csv", "w") as csvfile:
        file = csv.writer(csvfile)
        file.writerow(["World Rank", "Country", "2005 Population"])
        file.writerows(world_pop_2005(url))
        
data_to_csv(url)