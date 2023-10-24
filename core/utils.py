import random

def updateString(value_string, user_input):
    if not value_string:
        value_string = ""
    if len(value_string) < 6:
        value_string += user_input
        value_string += str(random.randint(0,9))
        return value_string
    else:
        return value_string

def isPalindrome(s):
    return s == s[::-1]