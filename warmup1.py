#Warmup 1
def sleep_in(weekday, vacation):
    '''
    The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
    We sleep in if it is not a weekday or we're on vacation. 
    Return True if we sleep in.
    '''
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    '''
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
    We are in trouble if they are both smiling or if neither of them is smiling. 
    Return True if we are in trouble.
    '''
    return a_smile == b_smile

def sum_double(a, b):
    '''
    Given two int values, return their sum. 
    Unless the two values are the same, then return double their sum.
    '''
    if a == b:
        return 2*(a + b)
    else:
        return a + b

def diff21(n):
    '''
    Given an int n, return the absolute difference between n and 21, 
    except return double the absolute difference if n is over 21.
    '''
    diff = abs(n-21)
    if n > 21:
        return 2*diff
    else:
        return diff

def parrot_trouble(talking, hour):
    '''
    We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
    We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
    Return True if we are in trouble.
    '''
    return (hour < 7 or hour > 20) and talking

def makes10(a, b):
    '''
    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
    '''
    sum = a + b
    return a == 10 or b == 10 or sum == 10

def near_hundred(n):
    '''
    Given an int n, return True if it is within 10 of 100 or 200. 
    Note: abs(num) computes the absolute value of a number.
    '''
    return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
    '''
    Given 2 int values, return True if one is negative and one is positive. 
    Except if the parameter "negative" is True, then return True only if both are negative.
    '''
    if negative:
        return a<0 and b <0
    else:
        return (a > 0 and b < 0) or ( a < 0 and b > 0)
    
def not_string(string):
    '''
    Given a string, return a new string where "not " has been added to the front. 
    However, if the string already begins with "not", return the string unchanged.
    '''
  if str[0:3] == 'not':
    return string
  else:
    return 'not ' + string

def missing_char(str, n):
    ''' 
    Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
    The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
    '''
    first = str[:n]
    second =str[n+1:]
    return first + second

def front_back(str):
    '''
    Given a string, return a new string where the first and last chars have been exchanged.
    '''
    front = str[:1]
    middle = str[1:-1]
    end = str[-1:]
    if len(str) <= 1:
        return str
    else:
        return end + middle + front

def front3(str):
    '''
    Given a string, we'll say that the front is the first 3 chars of the string. 
    If the string length is less than 3, the front is whatever is there. 
    Return a new string which is 3 copies of the front.
    '''
    if len(str) <= 3:
        return str*3
    else:
        return str[:3]*3