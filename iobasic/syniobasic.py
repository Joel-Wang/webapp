#! python3
# -*- coding: utf-8 -*-
#datetime模块中包含一个datetime类，通过  from datetime import datetime  语句 ，
#导入的才是datetime这个类，import os为导入操作系统模块
from datetime import datetime
import os
#读取当前目录的路径记为pwd
pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')#打印列表表头
print('------------------------------------------------------------')#打印分割线

#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺
#序。 它不包括 '.' 和'..' 即使它在文件夹中。
'''
for in循环语句可以遍历任何序列的项目，如一个列表或者一个字符串，如：
for letter in 'python'，即为遍历'python'字符串的每个字母

'''
for f in os.listdir(pwd):
    fsize = os.path.getsize(f)#获得文件大小，单位byte
    #1）datetime：举个例子，格式为2015-04-19 12:20:00
    #2）把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，timestamp相当于对
    #	epoch time的秒数，可以认为  timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00 时区，
    #	timestamp是一个浮点数。
    #3）fromtimestamp()将timestamp转化为datetime格式时间
    #4）os.path.getmtime（文件名）获取文件的创建时间
    #5）strftime()，实在懒得查啥意思。根据猜想，文件名应为将时间转换为字符串，括号里为格式
    #6）所以最终mtime为文件创建的datetime格式时间
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    #判断对应文件f是否为目录（文件夹），如果是文件夹在末尾输出/，否则输出空格
    flag = '/' if os.path.isdir(f) else ''
    #打印出文件尺寸（占10位），创建时间，文件名，标识flag
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))