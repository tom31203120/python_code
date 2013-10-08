#!/usr/bin/env python
import re
import os 
import urllib
import urllib2

def getHtml(url):
    page = urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" width'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    print('----------------------')
    #print(imglist)
    print('----------------------')
    for imgre in imglist:
        try:
            urllib.urlretrieve(imgre,'%s.jpg'%x)
        except Exception,ex:
            print(Exception,":", ex)
            print(imgre)
        x+=1
domain = "http://101.36.88.162:8080"
def download(url, output):
    url = domain + url
    #print "downloading..."+url
    try:
        response = urllib2.urlopen(url)
        resourceFile = open(output,"wb")
        resourceFile.write(response.read())
        resourceFile.close()
    except:
        print "error downloaded" + url
    #print "downloaded"

def get_list_of_href(url):
    url = domain + url
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        #2.content
        content = response.read()
    except:
        print("dir-------error")
        return []
    # print content
    #mode = '\"([^\"]+'+ext+')\"'
    mode = 'HREF=\"([^\"]*)\"'
    #print('----------=============-------==-=-=-=-=-=-')
    #print(mode)
    pattern = re.compile(mode)
    strMatch = pattern.findall(content)
    #size = len(strMatch)
    #print "file num: "+str(size)
    strMatch = set(strMatch)
    if '/' in strMatch:
        strMatch.remove('/')
    #size = len(strMatch)
    #print "file num: "+str(size)
    strMatch = list(strMatch)
    return strMatch


def walk(href, cur_path='KTVDaren.v1'):
    #mkdir ktv_src
    #print(cur_path)
    try:
        os.mkdir(cur_path)
    except:
        return
    os.chdir("./"+cur_path)
    href_list = get_list_of_href(href)
    for href in href_list:
        if href in total:
            continue
        total.add(href)
        print(href)
        if href[-1] == '/':
            #dir = get_dir
            url = href[:-1]
            index = url.rfind("/")
            dir = url[index+1:]
            walk(href,dir)
        else:
            index = href.rfind("/");
            output = href[index+1:]
            download(href, output)
    os.chdir('../')


#if os.path.exist()
os.system('rm -rf KTVDaren.v1')
total = set()
total.add('/')
total.add('/KTVDaren.v1/')
walk('/KTVDaren.v1/')
#html = getHtml("http://tieba.baidu.com/p/1904141161?pid=24952618510#24952618510")
#getImg(html)
