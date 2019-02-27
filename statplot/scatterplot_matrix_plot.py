'''
Python module for generating statistical distribution plots.
'''
import matplotlib.pyplot as plt
import seaborn as sns



def scatterplot_matrix_plot(df) -> None:
    '''Display a scatterplot matrix for the df arg'''
    sns.pairplot(df)

    plt.subplots_adjust(left=0.08, right=0.95, bottom=0.08, top=0.90, wspace=0.10)
    plt.show()
