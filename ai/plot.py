import matplotlib.pyplot as plt
from IPython import display

# Enable interactive plotting mode
plt.ion()

def plot(scores, mean_scores):
    """
    Plots the scores and mean scores for the training of the Snake game AI.

    Parameters:
    scores (list): A list of scores for each game.
    mean_scores (list): A list of mean scores calculated over a window of games.

    Returns:
    None
    """
    display.clear_output(wait=True)
    display.display(plt.gcf())
    
    # Clear the current figure
    plt.clf()
    
    # Set plot title and labels with a larger font size for better readability
    plt.title('Training Progress', fontsize=16)
    plt.xlabel('Number of Games', fontsize=14)
    plt.ylabel('Score', fontsize=14)
    
    # Plot scores and mean scores with thicker lines
    plt.plot(scores, label='Score per Game', linewidth=2, color='blue')
    plt.plot(mean_scores, label='Mean Score', linewidth=2, color='orange')
    
    # Add grid lines for better readability
    plt.grid(True)
    
    # Set the y-axis limit to start from 0
    plt.ylim(ymin=0)
    
    # Annotate the last point of scores and mean scores
    plt.annotate(f'{scores[-1]}', xy=(len(scores) - 1, scores[-1]), xytext=(len(scores) - 1, scores[-1] + 2),
                 textcoords='offset points', ha='center', fontsize=12, color='blue',
                 bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round,pad=0.5'))
    
    plt.annotate(f'{mean_scores[-1]}', xy=(len(mean_scores) - 1, mean_scores[-1]), xytext=(len(mean_scores) - 1, mean_scores[-1] + 2),
                 textcoords='offset points', ha='center', fontsize=12, color='orange',
                 bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
    
    # Add a legend to differentiate between scores and mean scores
    plt.legend(loc='upper left', fontsize=12)
    
    # Show the plot without blocking the execution and pause for a short interval
    plt.show(block=False)
    plt.pause(0.1)
