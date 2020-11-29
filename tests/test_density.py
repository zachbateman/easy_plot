import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.density(df, xvar='Weight', show_rug=True)
    statplot.density(df, xvar='Weight', categoryvar='Size', show_rug=True)
    statplot.density(df, xvar=['Weight', 'Value', 'Value_2', 'Value_3'], show_rug=True)




if __name__ == '__main__':
    test_func()
