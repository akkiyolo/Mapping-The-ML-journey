### Multithreading 
### When to use multi threading
### I/O bound tasks:Tasks that spend more time waiting for I/O operations example: file operations
### concurrent execution: when you want to improve the throughput of your application by performing multiple operations together

## we can create 2 threads one to run the numbers function of the code and other to run the letters function of the code

import threading
import time

def print_numbers():
  for i in range(5):
    time.sleep(2)
    print(f"Numbers:{i}")

def print_letter():
  for letter in "abcde":
    time.sleep(2)
    print(f"Letters={letter}")

##create two threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
#to start the thread
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)


##output:
"""
Numbers:0
Letters=a
Numbers:1
Letters=b
Numbers:2
Letters=c
Letters=d
Numbers:3
Numbers:4
Letters=e
 time = 10.015857934951782
"""
## so this is the practical implementation of how time got reduced to half after using the concept of multithreading

