from Exceptions import WrongInputException, WrongMonthOrDayException, WrongNumOfWeeksException, WrongNumOfDaysMonthException
from datetime import date, datetime
import logging
import argparse

def make_month(string, month_dict):
    if string.isdigit():
        if int(string)>0 and int(string)<13:
            return int(string)
        else:
            logging.error(f"{datetime.today()}: WrongNumOfDaysMonthException raised!")
            raise WrongNumOfDaysMonthException(string,'month')
    elif string in month_dict:
        return month_dict.get(string)
    else: 
        logging.error(f"{datetime.today()}: WrongMonthOrDayException raised!")
        raise WrongMonthOrDayException(string,'month')

def make_weekday(string, weekday_dict):
    if string.isdigit():
            if int(string)>0 and int(string)<7:
                returnint(string)
            else:
                logging.error(f"{datetime.today()}: WrongNumOfDaysMonthException raised!")
                raise WrongNumOfDaysMonthException(string,'day')
    elif string in weekday_dict:
        return weekday_dict.get(string)
    else: 
        logging.error(f"{datetime.today()}: WrongMonthOrDayException raised!")
        raise WrongMonthOrDayException(string,'weekday')

def make_weekcount(string):
    if array[0].isdigit():
        if int(array[0])<6 and int(array[0])>0:
            return int(array[0])
        else: 
            logging.error(f"{datetime.today()}: WrongNumOfWeeksException raised!")
            raise WrongNumOfWeeksException(array[0])
    else: 
        logging.error(f"{datetime.today()}: WrongNumOfWeeksException raised!")
        raise WrongNumOfWeeksException(array[0])

month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
              'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
weekday_dict = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday':3, 'friday':4, 'saturday': 5, 'sunday':6}

logging.basicConfig(filename='Ex1.log.', filemode='a',
encoding='utf-8', level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('strings', metavar='N', type=str, nargs='*', help='Enter date in format: 2 monday march (you can enter weekday or month as a number)')

args = vars(parser.parse_args())
array=args.get('strings')


if len(array)==3:
    month=make_month(array[2], month_dict)
    weekday=make_weekday(array[1], weekday_dict)
    weekcount=make_weekcount(array[0])
elif len(array)==2:
    month=datetime.today().month
    weekday=make_weekday(array[1], weekday_dict)
    weekcount=make_weekcount(array[0])
elif len(array)==1:
    month=datetime.today().month
    weekday=datetime.today().weekday()
    weekcount=make_weekcount(array[0])
elif len(array)==0:
    month=datetime.today().month
    weekday=datetime.today().weekday()
    weekcount=1
else: 
    logging.error(f"{datetime.today()}: WrongInputException raised!")
    raise WrongInputException(len(array))

month_1day=date(datetime.today().year, month, 1)
goal_date=month_1day
if weekcount>1:
    for i in range(weekcount-1):
        goal_date=goal_date.replace(day=goal_date.day+7)
if goal_date.weekday()!=weekday:
    while goal_date.weekday()!=weekday:
        goal_date=goal_date.replace(day=goal_date.day+1)
print(f'Your date: {goal_date}')
logging.info(f'{datetime.today()}: Your date: {goal_date}')