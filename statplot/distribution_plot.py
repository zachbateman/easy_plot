'''
Python module for generating statistical distribution plots.
'''
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
import pandas
import datetime
from pprint import pprint as pp


PLOT_TITLE = 'STATPLOT TITLE'
LARGEST_FONTSIZE = 17
BIN_ORDER = []  # list of bins so that they get ordered as desired on x axis


def _bin_order(df):
    return sorted({bin for bin in df.BINS})


def swarmplot(df, ax):
    sns.set_style('whitegrid')
    ax.set_ylim([0, round(_get_upper_bound(df.RESULT.max()))])  # set ylim before plotting to ensure good swarmplot point spacing
    BIN_ORDER =  _bin_order(df) # list of unique bins

    point_size = 75 / (len(df) / len(set(df['BINS'])))
    ax = sns.swarmplot(x='BINS', y='RESULT', data=df, ax=ax, size=point_size, order=BIN_ORDER)
    ax.set_xlabel('')
    ax.set_ylabel('RESULT', fontsize=LARGEST_FONTSIZE * 0.8)
    ax.tick_params(labelsize=10)

    line_width = 0.6
    for tick, text in zip(ax.get_xticks(), ax.get_xticklabels()):
        bin_name = text.get_text()
        mean = df[df.BINS == bin_name]['RESULT'].mean()
        ax.plot([tick-line_width/2, tick+line_width/2], [mean, mean], lw=5, color='#444455')

    ax.text(0.05, 0.97, 'Lines Indicate Bin Mean', bbox={'facecolor': '#dfdfee', 'edgecolor': '#444455'}, fontdict={'size': LARGEST_FONTSIZE * 0.7}, transform=ax.transAxes)

    ax.set_xlabel('X Label', fontsize=LARGEST_FONTSIZE * 0.8)


    def y_format(x, second_arg=None):  # idk... it is given a second arg that we don't need.
        return '{:,.0f}'.format(x)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(y_format))
    # return ax
    # plt.show()


def dist_plot(sorted_xy_lists, ax2):

    point_size = 400 / (len([val for xy_list in sorted_xy_lists for val in xy_list]) / len(sorted_xy_lists))
    max_x = 0
    for i, xy_list in enumerate(sorted_xy_lists):
        x, y = zip(*xy_list)
        ax2.scatter(x, y, s=point_size) #, color='r')
        # if i == 0:
            # ax2.scatter(x, y, s=10) #, color='r')
        # if i == 1:
            # ax2.scatter(x, y, s=10) #, color='b')  # marker='l'
        max_x = max(x) if max(x) > max_x else max_x

    upper_limit = _get_upper_bound(max_x)
    ax2.set_xlim([0, upper_limit])
    ax2.set_xticks([upper_limit / 5 * i for i in range(0, 5)])
    ax2.set_xlabel('RESULT', fontsize=LARGEST_FONTSIZE * 0.8)

    ax2.yaxis.tick_right()
    ax2.set_yticks([i / 10 for i in range(1, 10)])  # arg needs to be a list
    ax2.set_yticklabels(['P90', '', '', '', 'P50', '', '', '', 'P10'])

    def x_format(x, second_arg=None):  # idk... it is given a second arg that we don't need.
        return '{:,.0f}'.format(x)

    ax2.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(x_format))

    ax2.xaxis.grid(which='major', alpha=0.8)
    ax2.yaxis.grid(which='major', alpha=0.8)

    LEGEND_LABELS = BIN_ORDER
    legend = ax2.legend(labels=LEGEND_LABELS,
        loc='upper left',
        bbox_to_anchor=(0.02, 1.0),
        frameon=True,
        shadow=True,
        framealpha=1.0,
        fontsize=LARGEST_FONTSIZE * 0.6)
    legend.get_frame().set_facecolor('#eeeeee')
    legend.get_frame().set_edgecolor('#888888')
    for index in range(20):  # arbitrarily large number of tries to cover all scenarios
        try:
            legend.legendHandles[index]._sizes = [point_size]  # specifies size of legend marker
        except:
            pass


def _get_upper_bound(num):
    '''Return half way or all the way to next highest "order of magnitude" number'''
    for mag_order in range(0, 10):
        if num <= 0.5 * (10 ** mag_order):
            return 0.5 * (10 ** mag_order)
        elif num <= 10 ** mag_order:
            return 10 ** mag_order


def add_bins(df):
    '''Adds text descriptions binning each point'''
    bin_col = df[BIN_COLUMN].tolist()
    bins = []
    for value in bin_col:
        bins.append(value)
        # if statements to handle undesired BIN_COLUMN values
    df['BINS'] = bins
    return df


def create_plot_objects():
    fig = plt.figure(figsize=[10, 6])
    gs = gridspec.GridSpec(1, 2, width_ratios=[5, 3])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    return fig, ax1, ax2


def make_distplot_data(data):
    return [(val, (i+1)/len(data)) for i, val in enumerate(sorted(data))]



def distribution_plot(df, bin_col: str='', result_col: str='', bin_order: list=[]):
    fig, ax1, ax2 = create_plot_objects()

    df['BINS'] = df[bin_col]
    df['RESULT'] = df[result_col]

    swarmplot(df, ax1)

    dist_data = []

    if bin_order == []:
        bin_order = _bin_order(df)

    for bin in bin_order:
        filtered_data = df[df[bin_col] == bin][result_col].tolist()
        if len(filtered_data) > 0:
            dist_data.append(make_distplot_data(filtered_data))

    dist_plot(dist_data, ax2)

    tick_size = LARGEST_FONTSIZE * 0.7
    plt.setp(ax1.get_xticklabels(), fontsize=tick_size)
    plt.setp(ax1.get_yticklabels(), fontsize=tick_size)
    plt.setp(ax2.get_xticklabels(), fontsize=tick_size)
    plt.setp(ax2.get_yticklabels(), fontsize=tick_size)

    fig.suptitle(PLOT_TITLE, fontsize=LARGEST_FONTSIZE, y=0.96)
    ax1.set_ylabel(result_col)
    ax1.set_xlabel(bin_col)
    ax2.set_xlabel(bin_col)

    plt.subplots_adjust(left=0.08, right=0.95, bottom=0.08, top=0.90, wspace=0.10)
    plt.show()



if __name__ == '__main__':
    data = pandas.read_excel('test.xlsx', converters={'col_1': str, 'col_2': str})
    data = add_bins(data)
    distribution_plot(data)
