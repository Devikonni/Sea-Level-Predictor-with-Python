import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
def draw_plot():
    df=pd.read_csv('epa-sea-level.csv')
    # Read data from file
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],label='Original Data') 
    # Create scatter plot
    res=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x_pred=pd.Series(range(1880,2051))
    y_pred=res.intercept+res.slope*x_pred
    plt.plot(x_pred,y_pred,'r',label='Best Fit:1880-2050')
    # Create first line of best fit
    # Create second line of best fit
    df_recent=df[df['Year']>=2000]
    res_recent=linregress(df_recent['Year'],df_recent['CSIRO Adjusted Sea Level'])
    x_recent=pd.Series(range(2000,2051))
    y_recent=res_recent.intercept+res_recent.slope*x_recent
    plt.plot(x_recent,y_recent,'g',label='Best Fit:2000-2050')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()