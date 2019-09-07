import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.histogram(df['Value'].tolist(), xvar='Testing Value', bins=30)




if __name__ == '__main__':
    test_func()
