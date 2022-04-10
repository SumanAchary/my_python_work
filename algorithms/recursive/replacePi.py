from cgitb import small
from re import S


def replace_pi(str):
    if len(str) == 0 or len(str) == 1:
        return str
    
    if str[0] == 'p' and str[1] == 'i':
        smallOutput = replace_pi(str[2:])
        return "3.14" + smallOutput
    
    else:
        smallOutput = replace_pi(str[1:])
        return str[0] + smallOutput
