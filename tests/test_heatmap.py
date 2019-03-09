import pandas
import sys
sys.path.insert(1, '..')
import statplot

def test_func():
    df = pandas.read_csv('test_data.csv')
    statplot.heatmap_plot(df)



if __name__ == '__main__':
    test_func()
