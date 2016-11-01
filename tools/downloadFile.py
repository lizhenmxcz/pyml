from urllib import request
from bs4 import BeautifulSoup
import os


def schedule(a, b, c):

    per = 100.0 * a * b / c

    if per > 100:
        per = 100

    print('%.2f%%' % per)


def download(url):
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    atag = soup.select("td > a")
    for i in range(1, 73):
        href = atag[i].attrs['href']
        new_path = "E:/dataset/hadoopbook/" + href[:4]
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        uurl = url + href
        subhtml = request.urlopen(uurl).read()
        subsoup = BeautifulSoup(subhtml, "html.parser")
        tag = subsoup.select("td > a")
        for a in tag[1:]:
            durl = uurl + a.attrs['href']
            request.urlretrieve(durl, "E:/dataset/hadoopbook/" + href[:4] + "/" + a.get_text(), schedule)


download("http://www1.ncdc.noaa.gov/pub/data/noaa/")
