import statplot
import pandas


def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.distribution_plot(df, bin_col='color', result_col='value')



if __name__ == '__main__':
    test_func()
