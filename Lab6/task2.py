import pandas as pd


def task2_1():
    df = pd.read_csv('NYC_Jobs.csv', sep=',')
    print(df['Agency'][:10])


def task2_2():
    data = pd.read_csv('NYC_Jobs.csv')
    pd.options.display.max_columns = 3
    print(data[['Agency', 'Business Title', 'Work Location 1']].to_string(index=False))


if __name__=="__main__":
    task2_1()
    task2_2()
