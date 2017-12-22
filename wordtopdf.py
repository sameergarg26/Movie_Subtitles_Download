import sys
import os
import hashlib
import requests

file_path = os.path.abspath(sys.argv[1])
# file_path = r"G:\Chill\Movies\Dunkirk (2017) 1080p\Dunkirk.2017.1080p.BluRay.H264.AAC-RARBG.mp4"
# print(file_path)


def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


root, extension = os.path.splitext(file_path)
if extension not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp", ".3g2"]:
    exit(-1)

if not os.path.exists(root + ".srt"):
    headers = {'User-Agent': 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/manojmj92/subtitle-downloader)'}
    # url = "http://sandbox.thesubdb.com/?action=download&hash=" + get_hash(file_path) + "&language=en"
    url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(file_path) + "&language=en"
    # print(url)
    # cv = input()
    response = requests.get(url, headers=headers)
    # b = bytearray()
    s = str(response.text)
    print('done....')
    with open(root + ".srt", "w") as subtitle:
        subtitle.write(s)
        # logging.info("Subtitle successfully downloaded for " + file_path)



