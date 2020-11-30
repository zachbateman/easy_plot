# Statplot

Statplot is a Python package built to provide easy and fast production-quality visualizations of statistical data.
Utilizes pandas dataframes as standard format for input data.

# Current Features

  - statplot.distribution(df)
    - Plot a "Distribution Plot": a swarmplot alongside a cumulative probability plot.
    - Usage:
        ```sh
        import pandas
        import statplot
        df = pandas.read_csv('test.csv')
        statplot.distribution(df, bin_col='Weight', result_col='Value')
        ```
    <img src="tests/images/distribution_plot_example.png" width="550px">

  - statplot.scatter(df)
    - Plot a scatter plot.
    - Usage:
        ```sh
        import pandas
        import statplot
        df = pandas.read_csv('test.csv')
        statplot.scatter(df, xvar='Value', yvar='Value_2', sizevar='Weight')
        ```
    <img src="tests/images/scatterplot_example.png" width="550px">

  - statplot.scatter_matrix(df)
    - Plot a matrix of scatter plots.
    - Usage:
        ```sh
        import pandas
        import statplot
        df = pandas.read_csv('test.csv')
        statplot.scatter_matrix(df)
        ```
    <img src="tests/images/scatterplot_matrix_example.png" width="550px">

  - statplot.heatmap(df)
    - Plot a heatmap.
    - Usage:
        ```sh
        import pandas
        import statplot
        df = pandas.read_csv('test.csv')
        statplot.heatmap(df)
        ```
    <img src="tests/images/heatmap_example.png" width="550px">


License
----
MIT
