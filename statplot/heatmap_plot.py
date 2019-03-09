'''
Python module for generating statistical distribution plots.
'''
import matplotlib.pyplot as plt
import seaborn as sns



def heatmap_plot(df, title='Heatmap Title') -> None:
    '''
    Display a heatmap for the df arg
    Turn into or make separate Hinton diagram too!!!
    '''
    correlations = df.corr()
    cmap = sns.diverging_palette(220, 20, n=15)  # alternatively, use 'coolwarm'
    ax = sns.heatmap(correlations, annot=True, fmt=',.2f', linewidths=3, cmap=cmap, center=0)
    ax.xaxis.tick_top()
    ax.figure.suptitle(title, y=0.96)

    plt.subplots_adjust(left=0.08, right=0.95, bottom=0.08, top=0.84, wspace=0.10)
    plt.show()
