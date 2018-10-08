array2 = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
array3 = []

def fun(array, resultArr):
    for i in array:
        if isinstance(i, list):
            fun(i, resultArr)
        else:
            resultArr.append(i)

fun(array2, array3)
print("Result array: ", array3)

