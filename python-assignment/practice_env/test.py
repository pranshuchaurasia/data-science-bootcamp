#Logging in python
import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("THis is my first time using logging")
l=[2,45,3,2,6,76,45,2,4,5]
for i in l:
    if i==2:
        logging.info(l)

# degub, warning, error, critical, info