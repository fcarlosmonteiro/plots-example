#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Simple Pandas Plot Example
This script creates a simple line plot using pandas with sample sales data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_sample_data():
    """Create a sample DataFrame with sales data."""
    dates = pd.date_range(end='today', periods=30)
    
    np.random.seed(42)  
    sales = np.random.randint(100, 200, size=30) + np.linspace(0, 50, 30)
    
    df = pd.DataFrame({
        'Date': dates,
        'Sales': sales
    })
    
    return df

def plot_sales_data(df, output_file="pandas_plot.png"):
    """
    Create a line plot of sales data using pandas.
    
    Args:
        df (pd.DataFrame): DataFrame with 'Date' and 'Sales' columns
        output_file (str): Path to save the output plot
    """
    # Set the style
    plt.style.use('seaborn')
    
    # Create figure and axis with specified size
    plt.figure(figsize=(12, 6))
    
    # Create the plot using pandas built-in plotting
    df.plot(
        x='Date',
        y='Sales',
        kind='line',
        marker='o',
        color='steelblue',
        linewidth=2,
        markersize=6
    )
    
    # Customize the plot
    plt.title('Daily Sales Over Last 30 Days', pad=20, size=14)
    plt.xlabel('Date', labelpad=10)
    plt.ylabel('Sales ($)', labelpad=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()

def main():
    # Create sample data
    sales_df = create_sample_data()
    
    # Create and save the plot
    plot_sales_data(sales_df)
    
    # Print the first few rows of the data
    print("\nSample of the data used:")
    print(sales_df.head())

if __name__ == "__main__":
    main() 