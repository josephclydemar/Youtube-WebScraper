import re
import requests
import json
import threading





def load_video_urls(json_file):
    data = None
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def get_video_html(video_url):
    response = requests.get(video_url)
    return response.text

def search_thumbnail_url(page_html):
    search_regex = re.compile(r'itemprop\=\"thumbnailUrl\" href\="https\:\/\/i.ytimg.com\/vi\/([0-9|a-z|A-Z|\=|\/|\;|\-|\:|\.|\?|\&|\'|\s|\>|\<]+)\"')
    matches = search_regex.finditer(page_html)
    return matches

def download_video_thumbnails(json_data):
    for d in json_data:
        video_html = get_video_html(d['url'])
        thumbnail_url_match = search_thumbnail_url(video_html)
        # print(thumbnail_url_match)
        # for t in thumbnail_url_match:
        #     print(t.group())
        for m in thumbnail_url_match:
            response = requests.get(m.group().split(' ')[1].split('=')[1].replace('"', ''))
            with open(f'./thumbnails/{d["id"]}.png', 'wb') as f:
                f.write(response.content)


data = load_video_urls('dataset_youtube-scraper_2023-11-25_01-56-16-764.json')
# print(len(data))
# haha = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
t1 = threading.Thread(target=download_video_thumbnails, args=(data[0:20],))
t2 = threading.Thread(target=download_video_thumbnails, args=(data[20:40],))
t3 = threading.Thread(target=download_video_thumbnails, args=(data[40:60],))
t4 = threading.Thread(target=download_video_thumbnails, args=(data[60:80],))
t5 = threading.Thread(target=download_video_thumbnails, args=(data[80:100],))



t1.start()
t2.start()
t3.start()
t4.start()
t5.start()







# with open('data.txt', 'w', encoding='utf-8') as f:
#     f.write(response.text)

