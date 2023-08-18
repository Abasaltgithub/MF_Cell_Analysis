import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
blue_file_path = '/Users/abasaltbahrami/My Drive/Company/My research/PlateReader_30min/Exp2/SMF.xlsx'
red_file_path = '/Users/abasaltbahrami/My Drive/Company/My research/PlateReader_30min/Exp2/CTR.xlsx'

# Read the Excel files using pandas
blue_data = pd.read_excel(blue_file_path)
red_data = pd.read_excel(red_file_path)

# Calculate the row-wise averages
blue_data['Average'] = blue_data.iloc[:, 1:].mean(axis=1)
red_data['Average'] = red_data.iloc[:, 1:].mean(axis=1)

# Add the 'Source' column to identify the dataset
blue_data['Source'] = 0
red_data['Source'] = 1

# Concatenate the datasets for plotting
combined_data = pd.concat([blue_data, red_data], ignore_index=True)

# Create the scatter plot with adjusted x-axis positions
ax = combined_data.plot(x='Source', y='Average', kind='scatter', figsize=(
    8, 6), color=combined_data['Source'].apply(lambda x: 'red' if x == 0 else 'blue'), marker='o')

# Set the x-axis tick labels
ax.set_xticks([0, 1])
ax.set_xticklabels(['SMF 30 min', 'CTR 30 min'])

plt.xlabel('Dataset')  # Replace with your desired label
plt.ylabel('Average Y-axis label')  # Replace with your desired label
plt.title('Average Plot of All Data Points')  # Replace with your desired title
plt.show()
