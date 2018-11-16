from multiprocessing import Process,Pipe

import time,os

def consumer(p,name):
    left,right = p
    left.close()
    while True:
        try:
          s = right.recv()
          print('%s 收到包子:%s' %(name,s))
        except EOFError:
          right.close()
          break



def producer(seq,p):
    left,right = p
    for i in seq:
        left.send(i)
    else:
        left.close()
    print()

if __name__=='__main__':
    left,right = Pipe()

    c1 = Process(target=consumer,args=((left,right),"c1"))
    c1.start()
    seq = (i for i in range(10))
    producer(seq,(left,right))
    left.close()
    right.close()
    c1.join()
    print('main thread')

