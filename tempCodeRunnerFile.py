import pandas as pd
import matplotlib.pyplot as plt

# Replace 'MF_96well.csv' with the actual filename of the exported CSV
csv_file_path = '/Users/abasaltbahrami/My Drive/Company/My research/MF_96well.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Set the desired height for the bar plots
desired_height = 300  # Set the desired height to 300

# Generate X indices for the plot
x_indices = list('ABCDEFGH')

# Create a figure with two subplots (dual-axis plot)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create a second axis (ax2) for the bar plots on the right
ax2 = ax1.twinx()

# Determine the number of rows to plot (minimum of available rows and 12)
num_rows_to_plot = min(12, df.shape[0])

# Create the bar plots on the second axis (ax2) with the desired height and gray edge color
for _ in range(num_rows_to_plot):
    bars = ax2.bar(x_indices, [desired_height] * len(x_indices),
                   color='none', edgecolor='lightgray', hatch='', alpha=0.6)  # Set hatch pattern

# Plot the available rows using line plots on top of the bar plots
for row_index in range(num_rows_to_plot):
    data_row = df.iloc[row_index, 0:8].values
    ax1.plot(x_indices, data_row, marker='o', label=f'Row {row_index + 1}')

# Set labels and title
ax1.set_xlabel('Columns')
ax1.set_ylabel('Magnetic field (µT)')
ax2.yaxis.set_visible(False)

# Move the legend outside the plot and adjust its position
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.show()
