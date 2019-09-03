from multiprocessing import Process
import os

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    #p.join()
    p2 = Process(target=f, args=('anlo',))
    p2.start()
    p2.join()