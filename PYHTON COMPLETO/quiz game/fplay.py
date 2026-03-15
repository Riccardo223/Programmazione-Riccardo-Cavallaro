import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

def result(partita):
    '''inputs must be boolean values. 0 stands for cooperate and 1 for defect'''
    if [0,0] == partita:
        points = [3,3]
    elif [0,1] == partita:
        points = [0,5]
    elif [1,0] == partita:
        points = [5,0]
    else:
        points = [1,1]
        
    return points

def plot_games(p):
    'p = list with points'
    
    colors = ['red', 'yellow', 'green']
    values = [0, 1, 5]  # the unique values you want to map

    # Create colormap and normalization
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(boundaries=[-0.5, 0.5, 3, 6], ncolors=3)

    fig, ax = plt.subplots(figsize=(4, 6))  # width, height in inches

    # Display the image
    im = ax.imshow(p, cmap=cmap, norm=norm)

    # Add colorbar
    #cbar = fig.colorbar(im, ax=ax, ticks=values, shrink=0.8)
    #cbar.set_label("Value", rotation=270, labelpad=15)

    # Set custom column labels at the top
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Computer', 'You'])
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Optionally remove y-ticks (row labels)
    ax.set_yticks([])

    # Optional: remove tick lines for a cleaner look
    ax.tick_params(axis='both', length=0)

    # Make layout tight to fill space
    plt.tight_layout()
    plt.show()