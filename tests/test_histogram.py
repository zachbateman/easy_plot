import pandas
import sys
sys.path.insert(1, '..')
import easy_plot

def test_func():
    df = pandas.read_csv('test_data.csv')
    easy_plot.histogram(df['Value'].tolist(), xvar='Testing Value', bins=30)




if __name__ == '__main__':
    test_func()
