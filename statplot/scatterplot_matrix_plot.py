'''
Python module for generating statistical distribution plots.
'''
import matplotlib.pyplot as plt
import seaborn as sns



def scatterplot_matrix_plot(df, title='Scatterplot Matrix', regression_order=2) -> None:
    '''Display a scatterplot matrix for the df arg'''

    g = sns.PairGrid(df, diag_sharey=False)
    g.map_lower(sns.kdeplot)
    g.map_upper(sns.regplot, order=regression_order)
    g.map_diag(sns.kdeplot, lw=3, shade=True)


    g.fig.suptitle(title, y=0.96)
    plt.subplots_adjust(left=0.08, right=0.95, bottom=0.08, top=0.90, wspace=0.10)
    plt.show()
