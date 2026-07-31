"""Core plotting functions for viz_library.

Both functions take a pandas DataFrame and use matplotlib to draw a
simple, standard chart. Each function shows the plot and also returns
the matplotlib Axes object, in case the caller wants to customize it
further (e.g. add a title or save it to a file).
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cool, calm shades of green used across both chart types.
HISTOGRAM_FILL_COLOR = "#87A96B"    # eucalyptus green (bar fill)
HISTOGRAM_EDGE_COLOR = "#2F5D50"    # deep pine green (bar outline)
SCATTER_COLOR = "#87A96B"           # eucalyptus green (point fill)
SCATTER_EDGE_COLOR = "#2F5545"      # deep pine green (point outline)
SCATTER_BACKGROUND_COLOR = "#FFE066"  # soft yellow, used semi-transparent

# Font used for all chart text (labels, title, ticks).
FONT_NAME = "FreeSans"


def histogram(df, column):
    """Plot a histogram of a single numeric column in a DataFrame.

    Args:
        df: A pandas DataFrame containing the data.
        column: The name of the column to plot (must exist in df).

    Returns:
        The matplotlib Axes object for the plot.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")

    plt.rcParams["font.family"] = FONT_NAME
    fig, ax = plt.subplots()
    ax.hist(
        df[column].dropna(),
        color=HISTOGRAM_FILL_COLOR,
        edgecolor=HISTOGRAM_EDGE_COLOR,
    )
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {column}")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(color="lightgray", linewidth=0.5, alpha=0.5)

    plt.show()
    return ax


def scatterplot(df, x_column, y_column):
    """Plot a scatterplot comparing two numeric columns in a DataFrame.

    Args:
        df: A pandas DataFrame containing the data.
        x_column: The name of the column to use for the x-axis.
        y_column: The name of the column to use for the y-axis.

    Returns:
        The matplotlib Axes object for the plot.
    """
    if x_column not in df.columns:
        raise ValueError(f"Column '{x_column}' not found in DataFrame")
    if y_column not in df.columns:
        raise ValueError(f"Column '{y_column}' not found in DataFrame")

    plt.rcParams["font.family"] = FONT_NAME
    fig, ax = plt.subplots()
    ax.set_facecolor(SCATTER_BACKGROUND_COLOR)
    ax.patch.set_alpha(0.1)
    ax.scatter(
        df[x_column],
        df[y_column],
        color=SCATTER_COLOR,
        edgecolor=SCATTER_EDGE_COLOR,
    )
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f"{y_column} vs {x_column}")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.show()
    return ax
