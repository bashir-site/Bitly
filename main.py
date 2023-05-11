# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
from pathlib import Path
import argparse


BASE_URL = 'https://api-ssl.bitly.com/v4/'


def shorten_link(url, token):
    headers = { 
        'Authorization': 'Bearer {}'.format(token)
    }
    params = {
        'long_url': url
    }
    url = "{}shorten".format(BASE_URL)
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(link, token):
    headers = { 
        'Authorization': 'Bearer {}'.format(token)
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }
    url = "{}bitlinks/{}/clicks/summary".format(BASE_URL, link)
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    headers = { 
        'Authorization': 'Bearer {}'.format(token)
    }
    url = "{}bitlinks/{}".format(BASE_URL, url)
    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Программа проверяет количество переходов на сайт по биту')
    parser.add_argument('src', help="ссылка на сайт")
    args = parser.parse_args()
    env_path = Path('.') / '.env'
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    try:
        bitlink = args.src
        if is_bitlink(bitlink, bitly_token): 
            print('Битлинк', bitlink)
            print('По вашей ссылке прошли',count_clicks(bitlink, bitly_token),'раз')
        else:
            bitlink = shorten_link(bitlink, bitly_token)
            print("Сокращенный битлинк")
    except requests.exceptions.HTTPError as e:
        print("Ошибка", e.response.status_code)
  

