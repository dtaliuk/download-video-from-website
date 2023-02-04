import requests

video_url = input('video_url: ')
video_name = input('video_name: ') + '.mp4'


def download_video(url=''):
    try:
        # responce = requests.get(url=url)

        # with open(video_name, 'wb') as file:
        #     file.write(responce.content)

        responce = requests.get(url=url, stream=True)

        with open(video_name, 'wb') as file:
            for chunk in responce.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)

        return 'Video successfully downloaded!'

    except Exception as _ex:
        return 'Upps... Check the URL please!'


def main():
    print(download_video(url=video_url))


main()
