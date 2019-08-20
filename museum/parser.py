import requests
from bs4 import BeautifulSoup
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","museum.settings")
import django
django.setup()

from parsed_data.models import BigData

def parse_img():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get("http://www.tmon.co.kr/deal/1868865638?keyword=%EC%A0%84%EC%8B%9C%ED%9A%8C",headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')  

    imgs = soup.select('#image-wrapper > li > img') 
    return imgs

if __name__=='__main__':
    blog_data_dict = parse_img()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()