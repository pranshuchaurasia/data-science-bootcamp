import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
logging.info("This is my log with timestamp")
