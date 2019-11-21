'''
Python module for generating line plots.
'''
import matplotlib.pyplot as plt
import seaborn as sns



def densityplot(df, xvar='', x_label: str='', y_label: str='', show_rug: bool=False, size_minmax: tuple=(50  , 300), alpha: float=0.9, title='Densityplot', largest_fontsize: int=17, xlog=False, ylog=False, major_gridlines=False, minor_gridlines=False, xlim=[], ylim=[]) -> None:
    '''
    Display a density plot for the xvar arg (string or iterable of strings).
    '''
    # plot_kwargs = {'x': xvar, 'y': yvar}
    # plot_kwargs['sizes'] = size_minmax
    # if sizevar != '':
        # plot_kwargs['size'] = sizevar
    # else:
        # plot_kwargs['s'] = 200
    # if colorvar != '':
        # plot_kwargs['hue'] = colorvar
        # plot_kwargs['palette'] = 'coolwarm'

    colors = sns.color_palette(palette=None)
    if type(xvar) == str:
        ax = sns.kdeplot(df[xvar], shade=True)
        if show_rug:
            ax.plot(df[xvar], [0.0] * len(df), '|', color=colors[0])
    else:
        for i, var in enumerate(xvar):
            ax = sns.kdeplot(df[var], shade=True)
            if show_rug:
                ax.plot(df[var], [0.0] * len(df), '|', color=colors[i])

    ax.figure.suptitle(title, y=0.96, fontsize=largest_fontsize)
    if x_label != '':
        ax.set_xlabel(xvar, fontsize=largest_fontsize * 0.85)
    if y_label != '':
        ax.set_ylabel(y_label, fontsize=largest_fontsize * 0.85)

    ax.set_yticks([])

    if xlog:
        ax.set_xscale('log')
    if ylog:
        ax.set_yscale('log')

    ax.set_axisbelow(True)
    if major_gridlines:
        ax.grid(which='major', linestyle='-', linewidth=1, color='#bbbbbb')
    if minor_gridlines:
        ax.minorticks_on()
        ax.grid(which='minor', linestyle='-', linewidth=0.5, color='#cccccc')

    if xlim != []:
        ax.set_xlim(xlim)
    if ylim != []:
        ax.set_ylim(ylim)

    plt.subplots_adjust(left=0.08, right=0.95, bottom=0.08, top=0.90, wspace=0.10)
    plt.show()
