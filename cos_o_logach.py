import logging

# memo: nie nazywać pliku logging!!!!

logging.basicConfig(filename='cos_o_logach.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) #od# aby przestało logować wszystko poniżej i włacznie critical
'''
jest 5 poziomów logowania
    - debug (lowest)
    - info
    - warn
    - error
    - critical (highest)
'''
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.info('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))