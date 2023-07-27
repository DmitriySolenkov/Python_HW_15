from Exceptions import TriangleSideException, NotPositiveNumberException, NotNumberException, WrongAmountOfArgumentsException
from datetime import date, datetime
import logging
import argparse

# Enter 3 sides of triangle

logging.basicConfig(filename='Ex3.log.', filemode='a',
                    encoding='utf-8', level=logging.INFO)
parser = argparse.ArgumentParser()
parser.add_argument('strings', metavar='N', type=str,
                    nargs='*', help='(Enter your number)')

args = vars(parser.parse_args())
array = args.get('strings')
if len(array) != 3:
    logging.error(
        f"{datetime.today()}: WrongAmountOfArgumentsException raised!")
    raise WrongAmountOfArgumentsException(len(array), 3)
else:
    try:
        not_number = array[0]
        side_a = int(array[0])
        not_number = array[1]
        side_b = int(array[1])
        not_number = array[2]
        side_c = int(array[2])
        if (side_a < 0 or side_b < 0 or side_c < 0):
            if side_a < 0:
                num = side_a
            elif side_b < 0:
                num = side_b
            else:
                num = side_c
            logging.error(
                f"{datetime.today()}: NotPositiveNumberException raised!")
            raise NotPositiveNumberException(num)
    except ValueError:
        logging.error(f"{datetime.today()}: NotNumberException raised!")
        raise NotNumberException(not_number)
    if (side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_b + side_a):
        if (side_a == side_b and side_a == side_c):
            logging.info(f"{datetime.today()}: Equilateral")
            print("This triangle is equilateral")
        elif (side_a == side_b or side_a == side_c or side_b == side_c):
            logging.info(f"{datetime.today()}: Isosceles")
            print("This triangle is isosceles")
        else:
            logging.info(f"{datetime.today()}: Scalene")
            print("This triangle is scalene")
    else:
        logging.error(f"{datetime.today()}: TriangleSideException raised!")
        raise TriangleSideException(side_a, side_b, side_c)
