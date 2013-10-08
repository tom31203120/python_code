#! encoding=utf-8

import urllib2
import re
import os

def Download(url,output):
    print "downloading..."+url
    response = urllib2.urlopen(url)
    resourceFile = open(output,"wb")
    resourceFile.write(response.read())
    resourceFile.close()
    print "downloaded"

def Action(url,ext = "pdf",output = "./pdf/"):
    #1.domain
    index = url.rfind("/");
    domain = url[0:index+1];
    print domain
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    #2.content
    content = response.read()
    # print content

    #3.resource
    mode = '\"([^\"]+'+ext+')\"'
    print('----------=============-------==-=-=-=-=-=-')
    print(mode)
    pattern = re.compile(mode)
    strMatch = pattern.findall(content)
    size = len(strMatch)
    print "file num: "+str(size)
    strMatch = set(strMatch)
    size = len(strMatch)
    print "file num: "+str(size)
    strMatch = list(strMatch)

    for i in range(0,size,1):
        print strMatch[i]
        '''
        one = strMatch[i]
        partIndex = one.rfind('/')
        if not one.startswith('http://'):
            if -1!=partIndex:
                directDir = one[0:partIndex+1]
            else:
                directDir = ""
            #print directDir
            try:
                os.makedirs(output+"/"+directDir)
            except Exception,e:
                pass
            fileUrl = domain+one
            fileOutput = output+"/"+one
            print fileUrl
            print fileOutput
            Download(fileUrl,fileOutput)
        else:
            print one
            print "........."
            print one[partIndex:]
            fileOutput = output+"/"+one[partIndex:]
            print fileOutput
            Download(one,fileOutput)
    #5.download
        '''

if __name__=='__main__':
    print "download"
    url = "http://compgeom.cs.uiuc.edu/~jeffe/teaching/algorithms/";
    Action("http://tech.qq.com/","jpg");

