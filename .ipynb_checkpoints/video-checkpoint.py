import requests
# from multiprocessing import Pool
import subprocess
import re

def download(url):
    mlist = requests.get('http://jx.618g.com/?url='+url)
    text = mlist.text
    
    re_filename = re.compile(r'(?ms:.*?<title>(.+?)</title>$)')
    try:
        filename = re_filename.match(text).group(1)
    except AttributeError as e:
        print("except: ", e)
        print("Please check the element <title> in raw HTML file.")
    
    re_listaddr = re.compile(r'(?ms:.*?<iframe.*?\?url=(.*?\.m3u8)">)')
    try:
        listaddr = re_listaddr.match(text).group(1)
    except AttributeError as e:
        print("except: ", e)
        print("Please check the element <iframe src=\"...\"> in raw HTML file.")
    
    exp = 'ffmpeg -i "{x}" -vcodec copy -acodec copy ./{y}.mp4 -y'.format(x=listaddr, y=filename)
    proc = subprocess.run(exp,shell=True)
    return 1

url = 'https://www.iqiyi.com/v_19rrhs2sc0.html'
download(url)