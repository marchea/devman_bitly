import requests
import validators
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse


load_dotenv()
api_key = os.getenv("BITLY_GENERIC_TOKEN")


class BadUrl(Exception):
    pass


class TheresNoToken(Exception):
    pass


def get_short_url(key, url):
    api_resource = 'https://api-ssl.bitly.com/v4/bitlinks'

    headers = {
        'Authorization': 'Bearer ' + key,
    }

    json = {
        'long_url': url,
    }

    response = requests.post(api_resource, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['link']


def get_total_clicks(key, url):

    api_resource = f'https://api-ssl.bitly.com/v4/bitlinks/{crop_url(url)}/clicks/summary'

    headers = {
        'Authorization': 'Bearer ' + key,
    }

    json = {
        'unit': 'day',
        'units': '-1',
    }

    response = requests.get(api_resource, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(key, bitlink):
    api_resource = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'

    headers = {
        'Authorization': 'Bearer ' + key,
    }

    response = requests.get(api_resource, headers=headers)

    return response.ok


def crop_url(url):
    parsed_url = urlparse(url)
    new_url = parsed_url.netloc + parsed_url.path
    return new_url


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description='Программа получает на вход или длинную ссылку или битли-ссылку'
        )
        parser.add_argument('link', help='Ссылка')
        args = parser.parse_args()
        url = args.link

        if not validators.url(url):
            raise BadUrl()

        if api_key is None:
            raise TheresNoToken()

        cropped_url = crop_url(url)

        if not is_bitlink(api_key, cropped_url):
            short_url = get_short_url(api_key, url)
            print(short_url)
        else:
            total_clicks = get_total_clicks(api_key, url)
            print(f'Количество переходов по ссылке битли: {total_clicks}')

    except BadUrl:
        exit("Ошибка: Введена некорректная ссылка.")

    except TheresNoToken:
        exit("Ошибка: Проблемы с токеном.")

    except requests.exceptions.HTTPError as error:
        exit("Ошибка при обращении к ресурсу Bitly: {0}".format(error))

    except requests.exceptions.ConnectionError as error:
        exit("Ошибка соединения: {0}".format(error))

    except Exception as error:
        exit("Что-то пошло не так...\n{0}".format(error))
