#-*- coding:UTF-8 -*-
#!usr/bin/python


f = open("adress.txt")             # 返回一个文件对象
result_f = open("result.txt","w+")  
lines = len(f.readlines())        #获取文件行数
print("共有%d行文件"% lines)
for line in open("adress.txt"):
  
  newline = '-'.join(line.split())
  print(newline)
  result_f.write(newline+'\n')
 
f.close() 
result_f.close();