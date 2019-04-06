import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.scatterplot(df, xvar='Value', yvar='Value_2', sizevar='Weight')



if __name__ == '__main__':
    test_func()
