# -*- coding:utf-8 -*-
import os


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
    return all_the_text


if __name__ == '__main__':
    filePath = "E:\\NotBassRes\\"
    emailPath = eachFile(filePath) #遍历目录下所有文件
    email = []
    for path in emailPath:
        text = readFile(path) #读取文件内容
        text = text.replace('\n', ' ')
        email.append(text)
    for i in range(50):
        while True:
            fname = 'E:\\NotBassRemove\\NotBassRemove.txt'
            if os.path.exists(fname):
                # print "Error:" + fname + " already exists"
                break
            else:
                break
        fp = open(fname, 'a')
        fp.write(str(email[i]) + '\n')
        fp.close()


