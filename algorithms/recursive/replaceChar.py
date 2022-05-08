from cgitb import small


def replaceChar(str, a, b):
    if len(str) == 0:
        return str
    smallOutput = replaceChar(str[1:], a, b)
    if str[0] == a:
        return b + smallOutput
    else:
        return str[0] + smallOutput
