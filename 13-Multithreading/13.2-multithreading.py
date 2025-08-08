### Multithreading 
### When to use multi threading
### I/O bound tasks:Tasks that spend more time waiting for I/O operations example: file operations
### concurrent execution: when you want to improve the throughput of your application by performing multiple operations together

import threading
import time

def print_numbers():
  for i in range(5):
    print(f"Numbers:{i}")

def print_letter():
  for letter in "abcde":
    print(f"Letters={letter}")

t=time.time()
print_numbers()
print_letter()
finished_time=time.time()-t
print(finished_time)

