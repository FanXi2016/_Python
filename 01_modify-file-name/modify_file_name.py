import os
import re
import sys

## os.listdir(path='.'): 通过list的方式, 返回目录路径下所有的文件名(不包括'.'和'..').
fileList = os.listdir(r"./sourcecode/")

# 输出此文件夹中包含的文件名称
#print("修改前：" + str(fileList[1]))

## os.getcwd(): 以字符串形式, 返回当前目录.
CurrentPath = os.getcwd() + os.sep + 'sourcecode'

# 将当前工作目录修改为待修改文件夹的位置
#os.chdir(r"./sourcecode0904")

# 名称变量
num = 0
# 遍历文件夹中所有文件
for fileName in fileList:
    oldname=CurrentPath + os.sep + fileList[num]

    filename='VDS_'+fileList[num]
    print(filename)
    newname=CurrentPath + os.sep + filename

    ## os.rename(src, dst): 重命名文件或者目录, 如果dst存在, 则操作失败.
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    num = num + 1
print("***************************************")

# 刷新
sys.stdin.flush()

