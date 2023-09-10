import matplotlib.pyplot as plt
import numpy as np

# Data for the first set
tubulin_actin_MF = [0.1274, 0.2030, 0.2814, 0.1565, 0.1005, 0.0171]

# Data for the second set
tubulin_actin_CTR = [0.5143, 0.4540, 0.4658, 1.0645, 0.5305, 0.3167]

# Calculate means and standard deviations
mean_1 = np.mean(tubulin_actin_MF)
std_dev_1 = np.std(tubulin_actin_MF)

mean_2 = np.mean(tubulin_actin_CTR)
std_dev_2 = np.std(tubulin_actin_CTR)

# Labels for the x-axis (file names)
file_labels = ["480 $\mu$T", "Control"]

# Bar positions
x = [1, 2]  # x-coordinates of your bars

# Width of the bars
width = 0.35

# Define colors for the bars (orange and another color)
colors = ['orange', 'dodgerblue']

# Create the figure and axes objects
fig, ax = plt.subplots()

# Create bars for the means with error bars representing standard deviations
bars1 = ax.bar(x, [mean_1, mean_2], width, yerr=[
               std_dev_1, std_dev_2], capsize=5, color=colors)

# Set the x-axis labels
ax.set_xticks(x)
ax.set_xticklabels(file_labels)

# Add labels, title, and legend
ax.set_xlabel('Experimental Samples')
ax.set_ylabel('Tubulin/Actin Ratio (Mean)')
ax.set_title(
    'Tubulin/Actin Ratios Following a 2H Nocodazole Treatment in A7R5 Cells', fontsize=10)

# Scatter the data points for "MF" as triangles (marker='v')
ax.scatter([1] * len(tubulin_actin_MF), tubulin_actin_MF,
           color='black', label='Data Points MF', marker='v')

# Scatter the data points for "Control" as circles (default marker='o')
ax.scatter([2] * len(tubulin_actin_CTR), tubulin_actin_CTR,
           color='black', label='Data Points Control')

# Show the legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
