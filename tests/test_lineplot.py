import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.lineplot(df, xvar='Weight', yvar=['Value', 'Value_2', 'Value_3'])
    statplot.lineplot(df, xvar='Value', yvar='Size', hue='Weight')



if __name__ == '__main__':
    test_func()
