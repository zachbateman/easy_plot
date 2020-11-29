import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    df['GROUP'] = df['identifier'].map(lambda s: s[0])
    df['NORMALIZED_X'] = df['identifier'].map(lambda s: float(s[1]))
    statplot.trend(df, xvar='NORMALIZED_X', yvar='Value', binvar='GROUP', ylog=True)



if __name__ == '__main__':
    test_func()
