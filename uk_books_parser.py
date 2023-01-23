import requests
from bs4 import BeautifulSoup

headers = {'User-agent':  'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'}

for i in range(1, 9):
    url = f'https://kazka.eu/collections/kazky?page={i}'

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.content, features='html.parser')

    images = soup.find_all('img', class_='motion-reduce')

    for image in images:
        link = 'https:' + image.get('srcset').split(' ')[-2].split(",")[1]
        print(link)
        img_data = requests.get(link).content
        with open(f'pics/{link.split("v=")[1]}.jpg', 'wb') as handler:
            handler.write(img_data)
