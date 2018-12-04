import pandas as pd


def task2_1():
    df = pd.read_csv('NYC_Jobs.csv', sep=',')
    print(df['Agency'][:10])


def task2_2():
    data = pd.read_csv('NYC_Jobs.csv')
    print(data[['Agency', 'Business Title', 'Work Location 1']])


if __name__=="__main__":
    task2_1()
    task2_2()
