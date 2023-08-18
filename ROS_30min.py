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

# Create the initial plot with blue average
ax = blue_data.plot(
    x=blue_data.columns[0], y='Average', figsize=(10, 6), color='blue')

# Add red average to the plot
red_data.plot(x=red_data.columns[0], y='Average', ax=ax, color='red')

plt.xlabel('96-well')  # Replace with your desired label
plt.ylabel('a.u.')  # Replace with your desired label
plt.title('Average Plot of All Columns')  # Replace with your desired title
plt.legend(['SMF', 'CTR'])
plt.show()
