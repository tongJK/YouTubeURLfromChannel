"""
Description : get url of YouTube video from YouTue channel link.


By SinisterJK : https://github.com/tongjk


This code for education only, not for commercial purpose!!!
Enjoy ur develop :)
"""

import re
import urllib.request

color_map = ['\033[0;90m', '\033[0;91m', '\033[0;92m', '\033[0;93m', '\033[0;94m', '\033[0;95m',
             '\033[0;96m', '\033[0;97m']

def get_video_link(ch_url):

    re_filter = r'<a.*?/a>'
    read_url = urllib.request.urlopen(ch_url)
    all_links_temp = re.findall(re_filter, read_url.read().decode('utf-8'), re.MULTILINE)

    video_link_class = 'class="yt-uix-sessionlink yt-uix-tile-link'
    video_titles = []
    video_links = []

    for temp in all_links_temp:
        if video_link_class in temp:
            title_filter = r'title=".*?"'
            video_title_temp = re.findall(title_filter, temp, re.MULTILINE)
            video_titles.append(video_title_temp)
            url_filter = r'href=".*?"'
            video_link_temp = re.findall(url_filter, temp, re.MULTILINE)
            video_links.append(video_link_temp)

    for num, i in enumerate(video_titles):
        temp_title = str(i)
        temp_title = temp_title[9:-3]
        temp_link = str(video_links[num])
        temp_link = "https://www.youtube.com" + temp_link[8:-3]

        print(color_map[num % 8], num + 1, "Title: " + temp_title, "| link: " + temp_link)


get_video_link(ch_url)
