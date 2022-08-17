import logging

logging.basicConfig(filename="test4.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

try:
    logging.info("Trying to read te file")
    with open("pran.txt","r"):
        logging.info("successfully have read the file")
except Exception as e:
    logging.critical("This is a critical error for us")
    logging.error(e)
    logging.exception(e)