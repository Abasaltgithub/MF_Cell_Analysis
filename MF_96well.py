import pandas as pd
import matplotlib.pyplot as plt

# Replace 'MF_96well.csv' with the actual filename of the exported CSV
csv_file_path = '/Users/abasaltbahrami/My Drive/Company/My research/MF_96well.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Extract data from row 6 and columns A to H
data_row6 = df.iloc[5, 0:8].values  # Convert the data to a NumPy array

# Extract data from row 11 and columns A to H
data_row11 = df.iloc[10, 0:8].values  # Convert the data to a NumPy array

# Set the desired height for the bar plots
desired_height = 0.5  # Adjust this value to your desired height

# Generate X indices for the plot
x_indices = list('ABCDEFGH')

# Create a figure with two subplots (dual-axis plot)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create the line plot on the first axis (ax1) on the left for row 6
ax1.plot(x_indices, data_row6, marker='o', color='green',
         linestyle='-', label='MF row 6 (center row)')
ax1.set_ylabel('Magnetic field (µT)')

# Create a second axis (ax2) for the bar plot on the right
ax2 = ax1.twinx()

# Create the bar plot on the second axis (ax2) for row 6
bars = ax2.bar(x_indices, [desired_height] * len(x_indices),
               color='lightgray', alpha=0.6, label='96-well')

# Remove y-axis ticks and labels for the bar plot (ax2)
ax2.yaxis.set_visible(False)

# Create the line plot on the first axis (ax1) on the left for row 11
ax1.plot(x_indices, data_row11, marker='x', color='blue',
         linestyle='--', label='MF row 12 (last row)')

# Combine the legends from both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

# Display the plot
plt.show()
