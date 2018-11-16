import multiprocessing

def foo():
    q.put([11, 'hello', True])
    print(q.qsize())

q=multiprocessing.Queue()

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo, args=())
    p.start()
    foo() #主进程执行一下函数就可以访问到了
    print(q.get())