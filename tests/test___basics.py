
import sys
sys.path.insert(1, '..')
import easy_plot
from easy_plot import PlotData, Visualizer


# easy_plot.plot('test_data.csv')

data = PlotData.load('test_data.csv')

# Visualizer(data).scatter()
# Visualizer(data).heatmap(title='Data Correlation Heatmap')
# Visualizer(data).distribution(title='Data Distribution')
# Visualizer(data).density()# title='Data Density')
# Visualizer(data).scatter_matrix()
Visualizer(data).histogram()
