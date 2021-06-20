import requests
from bs4 import BeautifulSoup as bs4
from .parser import parser    as p





def scrape_weapon_info():
    return p.parse_weapon_info(bs4(requests.get('https://apexlegends.fandom.com/wiki/Weapon').text, 'lxml'))

def scrape_grenade_info():
    return p.parse_grenade_info(bs4(requests.get('https://apexlegends.fandom.com/wiki/Grenade').text, 'lxml'))
