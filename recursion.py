def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


def toStr(n, base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base, base) + convertString[n % base]



def rev_string(str):
    if len(str) == 0:
        return ''
    return rev_string(str[1:]) + str[0]


def removeWhite(str):
    while len(str) > 0:
        if str[0].isalnum():
            break
        str = str[1:]
    if len(str) == 0:
        return ''
    return str[0] + removeWhite(str[1:])


def isPal(str):
    if len(str) == 0:
        return True
    if str[0] != str[-1]:
        return False
    return isPal(str[1:-1])

