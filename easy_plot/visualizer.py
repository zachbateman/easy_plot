'''
Python module handling the higher-level logic of turning data into a visualization.
'''
from .plotdata import PlotData

from .plots import contour, density, distribution, heatmap, histogram
from .plots import line, scatter, scatter_matrix, surface, trend


class Visualizer():
    '''
    This class turns an instance of PlotData into plots.

    Only uses PlotData object as input data and lets
    PlotData handles data storage/manipulation.
    '''

    def __init__(self, data):
        self.data = data


    def available_plots(self):
        print('Currently functioning plots:')
        for plot in ['density', 'scatter', 'scatter_matrix', 'distribution', 'heatmap']:
            print(f'   - {plot}')

    def autoplot(self):
        ...

    def bar_chart(self, *args, **kwargs):
        ...

    def bar_chart_hz(self, *args, **kwargs):
        ...

    def contour(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        yvar = kwargs.pop('yvar', self.data.y_var)
        zvar = kwargs.pop('zvar', self.data.z_var)
        contour.contour(self.data.data, xvar=xvar, yvar=yvar, zvar=zvar, *args, **kwargs)

    def density(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        title = kwargs.pop('title', f'{self.data.x_var} Density')
        density.density(self.data.data, xvar=xvar, title=title, *args, **kwargs)

    def heatmap(self, *args, **kwargs):
        heatmap.heatmap(self.data.data, *args, **kwargs)

    def histogram(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        title = kwargs.pop('title', f'{self.data.x_var} Histogram')
        histogram.histogram(self.data.data[xvar].tolist(), xvar=xvar, *args, **kwargs)

    def line(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        yvar = kwargs.pop('yvar', self.data.y_var)
        line.line(self.data.data, xvar=xvar, yvar=yvar, *args, **kwargs)

    def lollipop(self, *args, **kwargs):
        ...

    def scatter(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        yvar = kwargs.pop('yvar', self.data.y_var)
        scatter.scatter(self.data.data, xvar=xvar, yvar=yvar, *args, **kwargs)

    def scatter_matrix(self, *args, **kwargs):
        scatter_matrix.scatter_matrix(self.data.data)

    def swarm(self, *args, **kwargs):
        ...

    def distribution(self, *args, **kwargs):
        bin_col = kwargs.pop('bin_col', self.data.bin_var)
        result_col = kwargs.pop('result_col', self.data.y_var)
        distribution.distribution(self.data.data, bin_col=bin_col, result_col=result_col)


    def surface(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        yvar = kwargs.pop('yvar', self.data.y_var)
        zvar = kwargs.pop('zvar', self.data.z_var)
        surface.surface(self.data.data, xvar=xvar, yvar=yvar, zvar=zvar, *args, **kwargs)

    def trend(self, *args, **kwargs):
        xvar = kwargs.pop('xvar', self.data.x_var)
        yvar = kwargs.pop('yvar', self.data.y_var)
        binvar = kwargs.pop('binvar', self.data.bin_var)
        trend.trend(self.data.data, xvar=xvar, yvar=yvar, binvar=binvar, *args, **kwargs)

    def map_folium(self, *args, **kwargs):
        '''Generate a Folium/Leaflet map'''
        lat_col, long_col = self.data.lat_long_columns
        if not lat_col and not long_col:
            print('Not able to identify columns for Latitude and Longitude.')


    def interactive_3d(self, *args, **kwargs):
        '''Launch interactive, 3D environment'''
        ...
