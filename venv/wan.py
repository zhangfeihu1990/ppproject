#-*- coding:UTF-8 -*-
#!usr/bin/python

tf = open('1166.txt')
lines = tf.readlines()
newfile = open('newf.txt','w+')
for idx in lines:
    newline = "-".join(idx.split())
    print('========='+newline)
    newfile.write(newline+'\n')

tf.close()
newfile.close()


