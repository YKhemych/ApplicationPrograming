import sys


class NegativeValue(Exception):
    pass

def division(fNum, sNum):
    if float(fNum % sNum) == 0:
        return 1
    else:
        return 0


firstNum = float(input("Enter first num - "))
secondNum = float(input("Enter second num - "))
try:
    if (firstNum < 0) or (secondNum < 0):
        raise NegativeValue("Exception")
except NegativeValue as e:
    print(e)
    sys.exit(1)
else:
    if division(firstNum, secondNum) == 1:
        print("Without remnant")
    else:
        print("With remnant")



