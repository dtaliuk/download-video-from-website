import wget

video_url = input('video_url: ')
video_name = input('video_name: ') + '.mp4'


def download_wget(url=''):
    try:
        wget.download(url=url, out=video_name)

        return 'Video successfully downloaded!'

    except Exception as _ex:

        return 'Upps... Check the URL please!'


def main():
    print(download_wget(url=video_url))


main()
