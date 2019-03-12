'''
Python module providing Principal Component Analysis capability.
'''
import sklearn.decomposition
import statplot
import numpy
import matplotlib.pyplot as plt


def pca_screeplot(df):

    standardized_df = statplot.cleaning.standardize_df(df)
    pca = sklearn.decomposition.PCA().fit(standardized_df)

    y = numpy.std(pca.transform(standardized_df), axis=0) ** 2
    x = numpy.arange(len(y)) + 1

    plt.plot(x, y, 'o-')
    plt.xticks(x, df.columns, rotation=60)
    plt.ylabel('Variance')
    plt.show()
