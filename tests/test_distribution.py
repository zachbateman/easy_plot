import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.distribution(df, bin_col='Weight', result_col='Value', mean_line=True, median_line=True)



if __name__ == '__main__':
    test_func()
