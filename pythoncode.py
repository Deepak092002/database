import requests
from bs4 import BeautifulSoup as bs
import pandas
import argparse
import main

parser = argparse.ArgumentParser()
parser.add_argument("--dbname",help="enter the",type=str)
args = parser.parse_args()
url = 'https://www.easemytrip.com/hotels/hotels-in-goa.html'

hotel_list = []
main.connect(args.dbname)

req = requests.get(url)

soup = bs(req.content, 'html.parser')

all_hotels = soup.find_all('div', attrs={'class': 'listinghtl'})

for hotel in all_hotels:
    hotel_dict = {}
    hotel_dict["name"] = hotel.find('span', {'class': 'hotl-name-sct'}).text
    hotel_dict["price"] = hotel.find('span', {'class': 'pr-txt'}).text

    hotel_list.append(hotel_dict)
    main.insert_into_table(args.dbname,tuple(hotel_dict.values()))

df = pandas.DataFrame(hotel_list)
df.to_csv("makemytrip.csv")
main.get_hotel(args.dbname)