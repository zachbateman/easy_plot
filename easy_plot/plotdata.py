'''
Python module handling flexible data storage/analysis of various input formats for plotting.
'''
from .plots.scatter import scatter

import pandas
from pandas import DataFrame
import numpy as np

_DATAFRAME = 'DATAFRAME'
_VALUES = 'VALUES'
_LIST_OF_DICTS = 'LIST_OF_DICTS'
_LIST = 'LIST'




class PlotData():
    '''
    Possible input formats to handle:
    Excel filepath
    CSV filepath
    Pandas DataFrame
    List of dicts
    List of values
    Lists of values
    '''
    @classmethod
    def load(cls, *args):
        # print(args)
        if len(args) == 0:
            raise ValueError('No data provided to load!')
        elif len(args) == 1:
            args = args[0]
            if '.xlsx' in args:
                return PlotData(pandas.read_excel(args), _DATAFRAME)
            elif '.csv' in args:
                return PlotData(pandas.read_csv(args), _DATAFRAME)
            elif isinstance(args, DataFrame):
                return PlotData(args, _DATAFRAME)
            elif isinstance(args, list):
                if type(args[0]) in [str, float, int]:
                    return PlotData(args, _VALUES)
                elif isinstance(args[0], dict):
                    return PlotData(args, _LIST_OF_DICTS)
                else:
                    return PlotData(args, _LIST)
            else:
                raise ValueError('Not sure how to parse provided data!')
        else:
            return PlotData.load(args[0]) + PlotData.load(args[1:])


    def __init__(self, data, data_type):
        self.data = data
        self.data_type = data_type


    def __add__(self, other):
        if self.data_type == _DATAFRAME:
            return PlotData(self.data.append(other.data), _DATAFRAME)
        elif self.data_type == _LIST:
            return PlotData(self.data + other.data, _LIST)


    @property
    def lat_long_columns(self) -> tuple:
        '''Return (Latitude_col, Longitude_col) if both are available.  (None, None) otherwise.'''
        lat_col, long_col = None, None
        if self.data_type == _DATAFRAME:
            for col in self.data.columns:
                if 'latitude' in col.lower() and not lat_col:
                    lat_col = col
                if 'longitude' in col.lower() and not long_col:
                    long_col = col
        return lat_col, long_col if lat_col and long_col else None, None

    @property
    def numeric_cols(self):
        if self.data_type == _DATAFRAME:
            return [col for col, _type in dict(self.data.dtypes).items() if _type != np.dtype('O')]

    @property
    def category_cols(self):
        if self.data_type == _DATAFRAME:
            return [col for col, _type in dict(self.data.dtypes).items() if col not in self.numeric_cols]

    @property
    def bin_var(self):
        best_bin, last_num_bins = self.category_cols[0], 999
        for col in reversed(self.category_cols):
            num_bins = len(set(self.data[col].tolist()))
            if 1 < num_bins < last_num_bins:
                best_bin = col
                last_num_bins = num_bins
        return best_bin

    @property
    def x_var(self):
        try:
            return self.numeric_cols[0]
        except IndexError:
            print('No numeric columns detected!')

    @property
    def y_var(self):
        try:
            return self.numeric_cols[1]
        except IndexError:
            print('No second numeric column detected!')
        
    @property
    def z_var(self):
        try:
            return self.numeric_cols[2]
        except IndexError:
            print('No third numeric column detected!')

    def suggested_plot(self):
        if self.data_type == _DATAFRAME:
            numeric_cols = [col for col, _type in dict(self.data.dtypes).items() if _type != np.dtype('O')]
            if len(numeric_cols) == 2:
                scatter(self.data, xvar=numeric_cols[0], yvar=numeric_cols[1])
            elif len(numeric_cols) == 3:
                scatter(self.data, xvar=numeric_cols[0], yvar=numeric_cols[1], sizevar=numeric_cols[2])
            else:
                scatter(self.data, xvar=numeric_cols[0], yvar=numeric_cols[1], sizevar=numeric_cols[2], colorvar=numeric_cols[3])
        else:
            ...


    def to_excel(self, filename='Plot Data.xlsx'):
        if self.data_type == _DATAFRAME:
            self.data.to_excel(filename)
        elif self.data_type == _LIST:
            ...

    def to_csv(self, filename='Plot Data.csv'):
        if self.data_type == _DATAFRAME:
            self.data.to_csv(filename)
        elif self.data_type == _LIST:
            ...

