import logging

## logging settings

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  handlers=[
    logging.FileHandler("app.log"),
    logging.StreamHandler()
  ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
  result=a+b
  logger.debug(f"Adding{a}+{b}={result}")
  return result

def subtract(a,b):
  result=a-b
  logger.debug(f"subtracting{a}-{b}={result}")
  return result

def multiply(a,b):
  result=a*b
  logger.debug(f"multiplying{a}*{b}={result}")
  return result

def divide(a,b):
  try:
    result=a/b
    logger.debug(f"dividing{a}/{b}={result}")
    return result
  except ZeroDivisionError:
    logger.error("Division by zero error")
    return None
  
add(10,15)
subtract(15,10)
multiply(5,3)
divide(15,5)
