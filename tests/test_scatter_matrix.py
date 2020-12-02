import pandas
import sys
sys.path.insert(1, '..')
import easy_plot

def test_func():
    df = pandas.read_csv('test_data.csv')
    easy_plot.scatter_matrix(df, title='Test Scatter Matrix')



if __name__ == '__main__':
    test_func()
