import numpy as np

def number_aproximation(A, z):
    index = np.abs(A-z).argmin()
    print(A[index])


def creatArray():
    A = np.random.randint(0, 400, (208,25))
    print(A)
    z=float(input("Input z: "))
    number_aproximation(A, z)

if __name__ == "__main__":
    creatArray()
