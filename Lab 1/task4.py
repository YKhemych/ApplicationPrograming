import sys

class NoSimpleDigits(Exception):
    pass

def array(fNum, sNum):
    try:
        if ((fNum < 1) or (sNum < 1)) or ((sNum - fNum) <= 1):
            raise NoSimpleDigits("NoSimpleDigits")
    except NoSimpleDigits as e:
        print(e)
        sys.exit(1)
    else:
        array = [];
        fNum += 1
        while sNum > fNum:
            numOfDivision = 0
            for i in range(2, fNum):
                if fNum % i == 0:
                    numOfDivision += 1
            if numOfDivision == 0:
                array.append(fNum)
            fNum += 1
        return array


firstNum = int(input("Enter first num - "))
secondNum = int(input("Enter second num - "))

array1 = []
array1 = array(firstNum, secondNum)

print(array1)
