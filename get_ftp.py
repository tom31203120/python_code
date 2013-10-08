# -*- coding: cp936 -*-
#!/usr/bin/env python

'''
Created on 2011-6-2

@author: zKF30352
'''



from ftplib import FTP
import shutil, sys, os, time
from datetime import datetime
from xml.etree import ElementTree as ET
from Dev_Data.LoadXml import loadItem






def main(host,ftpuser,pwd,traitname,startTime,logtype):

    #生成本地路径
    currentDir = os.path.dirname(sys.argv[0])
    
    ccfile = open(currentDir+'\\Dev_Cfg\\resultPath.txt', 'r')
    txns = ccfile.read()    
    ccfile.close()
    
    gtrBgnTime = startTime.replace(":", "_").replace('-', '_').replace(' ', '_')
    filepath = txns + 'log\\'+gtrBgnTime+traitname+'\\'+logtype+'\\'
    if not os.path.exists(filepath):     
        os.makedirs(filepath)
    
    
    
    #连接到FTP    
    try:    
        conn = FTP(host, ftpuser, pwd)
    except:
        print('FTP连接失败')
    #获取xml中配置的下载路径    
    fadName =getXml(logtype)
    conn.cwd(fadName)  
       
    os.chdir(filepath)  

    
    walk(conn,'.')
    
 

    
   
   
    
def walk(conn, next_dir):
        #next_dir路径，下级目录的路径
        conn.cwd(next_dir)
        print(next_dir)
        try:
            os.mkdir(next_dir)#这个是在当前工作路径创建文件夹
        except OSError:
            pass
        os.chdir(next_dir)#切换到当前路径为工作空间

        ftp_curr_dir = conn.pwd()
        local_curr_dir = os.getcwd()


        dir_res = []
        conn.dir('.', dir_res.append)  
    
        files = [f.split(None, 8)[-1] for f in dir_res if f.find('<DIR>')==-1]#隐患
        dirs = [f.split(None, 8)[-1] for f in dir_res if f.find('<DIR>')>=0][2:]
 
  
        for f in files:
            outf = open(f, 'wb')
            try:
                conn.retrbinary('RETR %s' % f, outf.write)

            finally:
                outf.close()
        print(local_curr_dir)
        print(ftp_curr_dir)
        for d in dirs:
            os.chdir(local_curr_dir)
            conn.cwd(ftp_curr_dir)
            walk(conn,d)
            
def getXml(logtype):
    #获取自动化运行结果目录
    currentDir = os.path.dirname(sys.argv[0])
    
    xmlPath = currentDir + "\\Dev_Cfg\\LOG_CFG.xml"
    xmlTree = ET.parse(xmlPath)
    fadName = loadItem(xmlTree, logtype+"/name")           #日志名
    
    return fadName
        




if __name__ == '__main__':
    print('------------------------日志生成开始-----------------------------')
    ftphost ='10.141.149.74'
    ftpusr='FtpUsr'
    ftppwd='111111'
  
    #生成fad日志
    startTime = datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")
    traitname=sys.argv[1]#特性名称
 
    #生成fad日志
    logtype="fad"
    main(ftphost,ftpusr,ftppwd,traitname,startTime,logtype)
    #生成fam日志
    logtype="fam"
    main(ftphost,ftpusr,ftppwd,traitname,startTime,logtype)
    #生成col日志
    logtype='collog'
    main(ftphost,ftpusr,ftppwd,traitname,startTime,logtype)
    
    print('------------------------日志生成结束-----------------------------')
