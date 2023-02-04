import requests

img_url = input('img_url: ')
img_name = input('img_name: ') + '.jpg'


def download_img(url=''):
    try:
        responce = requests.get(url=url)

        with open(img_name, 'wb') as file:
            file.write(responce.content)

        return 'Img successfully downloaded!'

    except Exception as _ex:
        return 'Upps... Check the URL please!'


def main():
    print(download_img(url=img_url))


main()
