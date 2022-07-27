import logging

logging.basicConfig(filename="test3.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

def div(a,b):
    return a,b

print((div(3,0)))