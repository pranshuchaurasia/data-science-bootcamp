import logging

logging.basicConfig(filename="test3.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

def devide(a,b):
    logging.info("The number entered by the user is %s and %s", a,b)
    try:
        logging.info("WE are into function")
        div=a/b
        logging.info("We have completed division operation")
        logging.info("result of code is %s", div)
    except Exception as e:
        logging.exception(e)

print((devide(3,8)))