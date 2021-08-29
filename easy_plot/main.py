'''
Highest-level functions for easy_plot.
'''
from .plotdata import PlotData

DATA = None

def load(*args):
    global DATA
    DATA = PlotData.load(*args)

    
def plot(*args):
    load(*args)
    DATA.suggested_plot()
