import os
from random import randrange

import requests
from dotenv import load_dotenv
from pprint import pprint

from main_function import download_image


def get_xcds_count():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comic_data = response.json()
    return comic_data['num']


def get_xcds_comics(number):
    url = f'https://xkcd.com/{number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_wall_upload_server(vk_token, vk_group):
    params = {
        'group_id': 219613989,
        'access_token': vk_token,
        'v': '5.81'
    }
    url = f'https://api.vk.com/method/photos.getWallUploadServer'
    response = requests.get(url, params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def main():
    load_dotenv()
    vk_client_id = os.getenv('VK_CLIENT_ID')
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')

    comics_number = randrange(get_xcds_count())
    img_url = get_xcds_comics(comics_number)['img']
    download_image(img_url, 'Images', prefix_name=comics_number)
    # print(get_xcds_comics(comics_number)['alt'])

     # url = 'https://api.vk.com/method/groups.get'
    # params = {
    #     'access_token': vk_access_token,
    #     'v': '5.81'
    # }
    # response = requests.get(url, params=params)
    # response.raise_for_status()
    # print(response.json())

    print(get_wall_upload_server(vk_access_token, vk_client_id))


if __name__ == '__main__':
    main()
