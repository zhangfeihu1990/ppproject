from multiprocessing import Pool
import time
def foo(n):
    print(n)
    time.sleep(1)

if __name__=='__main__':
    pool = Pool(5)
    before = time.time()
    for i in range(20):
      #pool.apply(func=foo,args=(i,))
      pool.apply_async(func=foo,args=(i,))

    pool.close()
    pool.join()
    after = time.time()
    print((after-before)/1000)
    print('ending')