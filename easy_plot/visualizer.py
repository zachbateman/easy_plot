'''
Python module handling the higher-level logic of turning data into a visualization.
'''
from .plotdata import PlotData



class Visualizer(self):
    '''
    Only uses PlotData object as input data.
    PlotData handles data storage/manipulation
    while Visualizer turns that into plots.
    '''

    def __init__(self, data):
        self.data = data


    def available_plots(self):
        ...

    def autoplot(self):
        ...

    def bar_chart(self):
        ...
        
    def bar_chart_hz(self):
        ...
        
    def lollipop(self):
        ...
        
    def scatter(self):
        ...
    
    def swarm(self):
        ...
        
    def distribution(self):
        ...

    
    def map_folium(self):
        '''Generate a Folium/Leaflet map'''
        lat_col, long_col = self.data.lat_long_columns
        if not lat_col and not long_col:
            print('Not able to identify columns for Latitude and Longitude.')


    def interactive_3d(self):
        '''Launch interactive, 3D environment'''
        ...
