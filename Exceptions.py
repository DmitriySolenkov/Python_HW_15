class UserException(Exception):
    pass

class WrongMonthOrDayException(UserException):
    def __init__(self,string,excpectation):
        self.string=string
        self.excpectation=excpectation

    def __str__(self):
        return f'{self.string} is not a {self.excpectation}'

class WrongInputException(UserException):
    def __init__(self, length):
        self.length=length

    def __str__(self):
        return f'Your input has {self.length} elements. Programm needs from 0 to 3.'

class WrongNumOfDaysMonthException(UserException):
    def __init__(self, num,string):
        self.num=num
        self.string=string

    def __str__(self):
        return f'Number {self.num} cannot be an amount of {self.string}'

class WrongNumOfWeeksException(UserException):
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f'There are maximum 5 weeks in a month! Your input is {self.num}'


class TriangleSideException(UserException):
    wrong_side = 0
    right_sides = (0, 0)

    def __init__(self, side_a, side_b, side_c):
        if side_a < side_b+side_c:
            self.wrong_side = side_a
            self.right_sides = (side_b, side_c)
        elif side_b < side_a+side_c:
            self.wrong_side = side_b
            self.right_sides = (side_a, side_c)
        else:
            self.wrong_side = side_c
            self.right_sides = (side_b, side_a)
        print()

    def __str__(self):
        return f'Side {self.wrong_side} is smaller than sum of sides {self.right_sides[0]} and {self.right_sides[1]}.' \
        'This triangle could not exist'


class NotPositiveNumberException(UserException):
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f'This number can not be negative: {self.num}'

class NotNumberException(UserException):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return f'{self.value} is not a number!'

class NotInBordersException(UserException):
    def __init__(self, num, lower,upper):
        self.num=num
        self.lower=lower
        self.upper=upper

    def __str__(self):
        if self.num<=self.lower:
            text='lower or equal'
            border=self.lower
        else:
            text='higher or equal'
            border=self.upper
        return f'Number {self.num} is {text} than {border} border'

class WrongAmountOfArgumentsException(UserException):
    def __init__(self, num, goal):
        self.num=num
        self.goal=goal

    def __str__(self):
        return f'Wrong amount of arguments! Need: {self.goal}. Got:{self.num}'