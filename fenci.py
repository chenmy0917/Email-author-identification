# -*- coding:utf-8 -*-
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import numpy as np
np.set_printoptions(threshold=np.inf)

def yuchuli(text):
    text = text.lower()
    qubiaodianRes = re.findall('[a-zA-Z]+',text)
    quxuciRes = []
    wordEngStop = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']
    for word in qubiaodianRes:
        if not word in wordEngStop and len(word) > 2:
            quxuciRes.append(word)
    bianxingRes = []
    porter_stemmer = PorterStemmer()
    for word in quxuciRes:
        ss = porter_stemmer.stem(word)
        bianxingRes.append(ss)
    return bianxingRes

def eachFile(filepath):
    emailPath = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        # print child.decode('gbk')  # .decode('gbk')是解决中文显示乱码问题
        emailPath.append(child.decode('gbk'))
    return emailPath

# 读取文件内容并打印
def readFile(filename):
    if not os.path.isfile(filename):
        raise TypeError(filename + " does not exist")

    all_the_text = open(filename).read()
    open(filename).close()
    # print all_the_text
    return all_the_text

#写文件
def writeToTxt(list_name,file_path):
    try:
        fp = open(file_path,"w")
        for item in list_name:
            fp.write(str(item) + '\n') #list中一项占一行
        fp.close()
    except IOError:
        print("fail to open file")



if __name__ == '__main__':
    # filePathNum = "E:\countRes\\countNum.txt"
    filePathHead = "E:\NotBassRes\\NotBassHead.txt"
    filePath = "E:\\NotBassEmail\\"
    emailPath = eachFile(filePath) #遍历目录下所有文件
    email = []
    for path in emailPath:
        text = readFile(path) #读取文件内容
        email.append(text)
    chuliRes = []
    for text in email:
        arrRes = yuchuli(text)
        strRes = ','.join(arrRes)
        chuliRes.append(strRes)
    print chuliRes
    vectorizer = TfidfVectorizer(min_df=1)
    vectorizer.fit_transform(chuliRes)
    all_the_head = vectorizer.get_feature_names()
    all_the_text = vectorizer.fit_transform(chuliRes).toarray()
    writeToTxt(all_the_head, filePathHead)
    # writeToTxt(all_the_text, filePathNum)
    for i in range(50):
        while True:
            fname = 'E:\NotBassRes\\NotBassRes' + str(i) + '.txt'
            if os.path.exists(fname):
                # print "Error:" + fname + " already exists"
                break
            else:
                break
        fp = open(fname, 'w')
        fp.write(str(all_the_text[i]))
        fp.close()
