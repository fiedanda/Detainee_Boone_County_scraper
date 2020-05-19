#!/usr/bin/env python
# coding: utf-8

# # Webscraper, Detainees in Boone County
#Libraries needed
from bs4 import BeautifulSoup
import requests
import requests_cache
from datetime import timedelta
from time import sleep
from models import Detainee
from peewee import DoesNotExist

requests_cache.install_cache(
    'cache',
    expire_after=timedelta(hours=24),
    allowable_methods=('GET', 'POST')
)

url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s'
URL = 'view-source:https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s?max_rows=100000'


r = requests.get(
    'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s',
    headers={'user-agent': "Not a snake"},
    params={"max_rows": 10000}
)

soup = BeautifulSoup(r.content, 'lxml')

def get_detainees_list(detainees_list):
    r = requests.post(
    'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s',
    headers={'user-agent': "Not a snake"},
    params={"max_rows": 10000}
    )

    r.raise_for_status()

    return r.concent


def extract_details(detainees_list):
    soup = BeautifulSoup(detainees_list, 'lxml')

    details_urls = []

    table = soup.find('tbody', id='mrc_main_table')

    td_all = table.find_all('td')

    for td in td_all:
        detail_url = td.find('a').attrs['href'] 
        details_urls.append(detail_url)

        return details_urls


def get_details_report(full_url):

    full_url = 'https://report.boonecountymo.org/' + rel_url

    r = requests.get(full_url)

    r.raise_for_status()

    return r.content



def exctract_info_from_details(detail_url):
    soup = BeautifulSoup(detail_url, 'lxml')

    tables = soup.find_all('table')

    detainee_info_table1 = tables.find('table', class_="collapse centered_table shadow responsive")

    detainee_info_table2 = tables.find('table', class_="collapse centered_table shadow")


    detainee_info_cells = detainee_info_table.find_all('td', class_="two td_left")

    Detainee_all_into = Detainee.create(
        case_numb=detainee_info_cells1[0].text.strip(),
        charge_description=detainee_info_cells1[1].text.strip(),
        charge_status=detainee_info_cells1[2].text.strip(),
        bail_amount=detainee_info_cells1[3].text.strip(),
        bond_type=detainee_info_cells1[4].text.strip(),
        court_date=detainee_info_cells1[5].text.strip(),
        court_time=detainee_info_cells1[6].text.strip(),
        juristriction_court=detainee_info_cells1[7].text.strip(),
        height=detainee_info_cells2[0].text.strip(),
        weight=detainee_info_cells2[1].text.strip(),
        sex=detainee_info_cells2[2].text.strip(),
        eyes=detainee_info_cells2[3].text.strip(),
        hair=detainee_info_cells2[4].text.strip(),
        race=detainee_info_cells2[5].text.strip(),
        age=detainee_info_cells2[6].text.strip(),
        city=detainee_info_cells2[7].text.strip(),
        state=detainee_info_cells2[8].text.strip()
        )

def main():
    for detainees_list in get_detainees_list():
        extracted_details = details_urls
        print(extracted_details)
        print(Detainee_all_into)
        sleep(3)

if __name__ == '__main__':
    main()