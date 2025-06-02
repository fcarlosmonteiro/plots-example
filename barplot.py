#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Bar Plot Example
This script creates a bar plot comparing execution times for different configurations.
"""

import numpy as np
import matplotlib.pyplot as plt

def create_bar_plot(configurations, times, output_file="time.png"):
    """
    Create a bar plot comparing execution times.
    
    Args:
        configurations (tuple): Configuration numbers
        times (list): Execution times in seconds
        output_file (str): Path to save the output plot
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Create positions for bars
    y_pos = np.arange(len(configurations))
    
    # Create bars
    plt.bar(y_pos, times, 
           align='center',
           alpha=0.8,
           color='steelblue',
           width=0.5,
           edgecolor='black')
    
    # Customize the plot
    plt.xticks(y_pos, configurations)
    plt.xlabel('Configuration')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time by Configuration')
    
    # Add value labels on top of bars
    for i, v in enumerate(times):
        ax.text(i, v + 0.1, f'{v:.2f}s',
                ha='center', va='bottom')
    
    # Adjust layout and save
    plt.tight_layout()
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()

def main():
    # Sample data
    configurations = (1, 2)
    execution_times = [3.06, 12.98]
    
    create_bar_plot(configurations, execution_times)

if __name__ == "__main__":
    main()
