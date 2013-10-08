#coding:utf-8
import binascii
import base64
import pyDes
from hashlib import md5

class DES:
    #IV必须是 8 字节长度的十六进制数
    iv = '1234567812345678'
    #key加密密钥长度，24字节
    key = '12345678'
    def __init__(self, iv, key):
        self.iv = iv
        self.key = key
    def encrypt(self, data):
        k = pyDes.des(self.key, pyDes.CBC, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(data)
        print("xxxxoriginxxxxxxxxxx")
        print(d)
        print('...............................')
        print "Encrypt00000000000000000ed:%r" % binascii.hexlify(d)
        #d = base64.encodestring(d)
        return d
    def decrypt(self, data):
        k = pyDes.des(self.key, pyDes.CBC, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
       # data = base64.decodestring(data)
        d = k.decrypt(data)
        return d
    '''
    def encrypt(self, data):
        k = pyDes.triple_des(self.key, pyDes.ECB, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(data)
        print("xxxxxxxxxxxxxx")
        #print(d)
        print('...............................')
        print "Encrypted:%r" % binascii.hexlify(d)
        #d = base64.encodestring(d)
        return d
    def decrypt(self, data):
        k = pyDes.triple_des(self.key, pyDes.CBC, self.iv, pad=None, padmode=pyDes.PAD_PKCS5)
       # data = base64.decodestring(data)
        d = k.decrypt(data)
        return d
    '''
if __name__ == '__main__':

    text = "l/5IKInHsFOZtAWtGseCbAVNojQ="
    sKey = "ktvdarenupyun"
    x = md5(sKey).hexdigest()
    print(x)
    print(x[0:8])

    data = text
    x = x[0:8]
    y = binascii.hexlify(x)
    '''
    print "Encryptxxxxxxed:%r" % x)
    #print "Encrypteyyyyyyyyyd:%r" % y)
    print(y)
    y = str(y)
    print(y)
    print(len(y))
    y = '3362313330386235'
    '''
    x = '3B1308B5'
    des = DES(x,x)
    encryptdata = des.encrypt(data.encode('utf-8'))
    print('...............................')
    # print "Encrypted:%r" % binascii.hexlify(encryptdata)
    print type(encryptdata)
    print  encryptdata
    decryptdata = des.decrypt(encryptdata)
    print decryptdata
