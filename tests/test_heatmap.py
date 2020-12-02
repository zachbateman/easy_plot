import pandas
import sys
sys.path.insert(1, '..')
import easy_plot

def test_func():
    df = pandas.read_csv('test_data.csv')
    easy_plot.heatmap(df, cluster=False)
    easy_plot.heatmap(df, cluster=True)



if __name__ == '__main__':
    test_func()
