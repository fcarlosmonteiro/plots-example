#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Line Plot Example
This script creates a line plot comparing two fitness functions over generations.
"""

import matplotlib.pyplot as plt
import numpy as np

def create_line_plot(generations, fitness1, fitness2, output_file="plot.png"):
    """
    Create a line plot comparing two fitness functions.
    
    Args:
        generations (list): List of generation numbers
        fitness1 (list): Values for first fitness function
        fitness2 (list): Values for second fitness function
        output_file (str): Path to save the output plot
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot both fitness functions
    plt.plot(generations, fitness1, label='Fitness Function 1', linewidth=2)
    plt.plot(generations, fitness2, label='Fitness Function 2', linewidth=2)
    
    # Customize the plot
    plt.legend()
    ax.set(xlabel='Generation', ylabel='Fitness')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Set title and adjust layout
    plt.title('Fitness Functions Comparison')
    plt.tight_layout()
    
    # Save and display the plot
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()

def main():
    # Sample data
    generations = list(range(201))  # 0 to 200
    
    # First fitness function values
    fitness1 = [1,1,0.770528,0.770528,0.770528,0.770528,0.68915,0.68915,0.68915,0.666422] + \
              [0.666422] * 30 + [0.452346] * 3 + [0.38783] * 14 + [0.179619] * 25 + \
              [0.16129] * 2 + [0.147361] * 50 + [0.02566] * 5 + [0.007331] * 62
    
    # Second fitness function values
    fitness2 = [1,1,0.990528,0.880528,0.800528,0.790528,0.69915,0.69915,0.68915,0.666422] + \
              [0.666422] * 30 + [0.452346] * 3 + [0.38783] * 14 + [0.179619] * 25 + \
              [0.16129] * 2 + [0.147361] * 50 + [0.02566] * 5 + [0.007331] * 59 + [0.010331] * 3

    create_line_plot(generations, fitness1, fitness2)

if __name__ == "__main__":
    main()