import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit (all data)
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_full = pd.Series(range(1880, 2051))
    y_pred_full = res_full.slope * x_pred_full + res_full.intercept
    plt.plot(x_pred_full, y_pred_full, 'r', label='Best Fit Line: All Data')

    # Create second line of best fit (from year 2000)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, 'green', label='Best Fit Line: 2000-Present')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return figure
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
