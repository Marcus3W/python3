# Basics of logging

import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stream_handler)

# Logging levels

print(logging.NOTSET)
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)


# Logging Errors and Messages

logger.debug("This is a debug message")

logger.log(logging.INFO, "This is an info message")

# Working example 1

import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
        
def division():
  logger.debug("Starting Division! ")
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend)
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
    return
  if divisor == 0:
    logger.error("Attempting to divide by 0!")
    return
  else:
    return dividend/divisor
result = division()
if result == None:
  logger.warning("The result value is None!")