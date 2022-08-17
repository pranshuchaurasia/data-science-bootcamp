#Logging in python
import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("THis is my first time using logging")
logging.warning("This will load warning message")
logging.error("THis is an error message")
l=[2,45,3,2,6,76,45,2,4,5]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning("They have found 2 in the list")
# debug(10), warning(30), error(40), critical(50), info (20)
logging.shutdown()