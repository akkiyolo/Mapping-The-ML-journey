'''
Real-world example:Multiprocessing for cpu bound processes
Scenario: factorial calculation
Factorial calculations, especially for large numbers , invlove significant computational work . Multiprocessing can be used to distribute the workload across multiple cores , involving performance.
'''

import multiprocessing
import math
import sys
import time

## increase the maximum number of digits for integer conversions

sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number

def compute_factorials(number):
  print(f"computing factorial of {number}")
  result=math.factorial(number)
  print(f"factorial of {number} is {result}")
  return result


if __name__=="__main__":
  numbers=[5000,6000,7000,8000]
  start_time=time.time()

  ## create a pool of worker processes

  with multiprocessing.Pool() as pool:
    results=pool.map(compute_factorials,numbers)

  end_time=time.time()

  print(f"Results : {results}")
  print(f"Time Taken: {end_time-start_time} seconds")


