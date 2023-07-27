from Exceptions import NotNumberException, NotInBordersException
from datetime import date, datetime
import logging
import argparse

# Complex or prime number

logging.basicConfig(filename='Ex2.log.', filemode='a',
                    encoding='utf-8', level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument('strings', metavar='N', type=str,
                    nargs='*', help='(Enter your number)')

args = vars(parser.parse_args())
array = args.get('strings')
if len(array) < 1:
    print("Empty input!")
    logging.critical(f"{datetime.today()}: Empty input!")
else:
    res = array[0]
    try:
        num = int(res)
        if (num <= 0 or num >= 100000):
            logging.error(f"{datetime.today()}: NotInBordersException raised!")
            raise NotInBordersException(num, 0, 100000)
    except ValueError:
        logging.error(f"{datetime.today()}: NotNumberException raised!")
        raise NotNumberException(res)
    if num == 1:
        print("This number is neither prime nor complex")
        logging.info(f"{datetime.today()}: Neither prime nor complex raised")
    elif num == 2:
        print("This number is prime")
        logging.info(f"{datetime.today()}: Prime")
    else:
        check = False
        for i in range(2, num):
            if num % i == 0:
                print("This number is complex")
                logging.info(f"{datetime.today()}: Complex")
                check = True
                break
    if check == False:
        print("This number is prime")
        logging.info(f"{datetime.today()}: Prime")
