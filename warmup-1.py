#CodingBat warmup1
#exercise 1
def sleep_in(weekday, vacation):
  """The parameter weekday is True if it is a weekday, and the parameter vacation is
True if we are on vacation. We sleep in if it is not a weekday or we're on
vacation. Return True if we sleep in."""
  if not weekday or vacation:
    return True
  else:
    return False
#or another way
def sleep_in(weekday, vacation):
  return(not weekday or vacation)

  
#exercise 2
def monkey_trouble(a_smile, b_smile):
  """We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if
each is smiling. We are in trouble if they are both smiling or if neither of
them is smiling. Return True if we are in trouble."""
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  else:
    return False
## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)
#exercise 3
def sum_double(a, b):
  """Given two int values, return their sum. Unless the two values are the same,
then return double their sum."""
  if a == b:
    return (a+b)*2
  else:
    return a+b
#or another option
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum
#exercise 4
def diff21(n):
  """Given an int n, return the absolute difference between n and 21, except return
double the absolute difference if n is over 21."""
  if n <= 21:
    return 21 - n
  else:
    return (n - 21)*2
#exercise 5
def parrot_trouble(talking, hour):
  """We have a loud talking parrot. The "hour" parameter is the current hour time in
the range 0..23. We are in trouble if the parrot is talking and the hour is
before 7 or after 20. Return True if we are in trouble."""
  if talking and hour < 7:
    return True
  elif talking and hour > 20:
    return True
  else:
    return False
#or another way
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +
 
#exercise 6

"""Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number."""
def near_hundred(n):
  if (n >= 90 and n <= 110) or (n >= 190 and n <= 210):
    return True
  else:
    return False
#exercise 7

"""Given 2 int values, return True if one is negative and one is positive. Except if
the parameter "negative" is True, then return True only if both are negative."""
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
#exercise 8

"""Given 2 ints, a and b, return True if one if them is 10 or if their
sum is 10."""
def makes10(a, b):
  if a==10 or b==10 or a+b==10:
    return True
  else:
    return False
#or another way
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)
#exercise 9

"""Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged."""
def not_string(str):
  if str[0:3]=="not":
    return str
  else:
    return ("not "+str)
#or
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3
#exercise 10
"""Given a non-empty string and an int n, return a new string where the char at
index n has been removed. The value of n will be a valid index of a char in
the original string (i.e. n will be in the range 0..len(str)-1 inclusive)."""
def missing_char(str,n):
    front=str[:n]
    back=str[n+1:]
    return front + back
result = missing_char("caro",2)
print(result)
#exercise 11
"""Given a string, return a new string where the first and last chars have
been exchanged."""
def front_back(str):
  if len(str)<=1:
    return str
  new_string=str[-1]+str[1:-1]+str[0]
  return new_string
result = front_back("t")
print(result)
def front_back(str):
  if len(str)<=1:
    return str
  middle_string=str[1:(len(str)-1)]
  new_string=str[-1]+middle_string+str[0]
  return new_string
result = front_back("crush")
print(result)
#exercise 12
"""
Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there. Return
a new string which is 3 copies of the front."""
def front3(str):
  if len(str)<=3:
    return str*3
  new_str=(str[0:3])*3
  return new_str
result=front3("christchurch")
print(result)
  
