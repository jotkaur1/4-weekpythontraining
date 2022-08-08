import threading
import os
def t1():
    print("task 1 assigned to thread {}".format(threading.current_thread().name))
    print("ID of task 1: {}".format(os.getpid()))
def t2():
    print("task 1 assigned to thread {}".format(threading.current_thread().name))
    print("ID of task 1: {}".format(os.getpid()))

print("ID of current process in main: {}".format(os.getpid()))

print("Name of main thread: {}".format(threading.current_thread().name))

#create thread
th1=threading.Thread(target=t1,name="T1")
th2=threading.Thread(target=t2,name="T2")

th1.start()
th1.start()
th1.join()
th1.join()
    
