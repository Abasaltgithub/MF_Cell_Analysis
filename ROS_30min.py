import pandas as pd
import matplotlib.pyplot as plt

# Define the file paths
blue_file_path = '/Users/abasaltbahrami/My Drive/Company/My research/PlateReader_30min/Exp2/SMF.xlsx'
red_file_path = '/Users/abasaltbahrami/My Drive/Company/My research/PlateReader_30min/Exp2/CTR.xlsx'

# Read the Excel files using pandas
blue_data = pd.read_excel(blue_file_path)
red_data = pd.read_excel(red_file_path)

# Create the initial plot in blue
ax = blue_data.plot(
    kind='line', x=blue_data.columns[0], y=blue_data.columns[1:], figsize=(10, 6), color='blue')

# Add lines from the red file in red
red_data.plot(
    kind='line', x=red_data.columns[0], y=red_data.columns[1:], ax=ax, color='red')

plt.xlabel('X-axis label')  # Replace with your desired label
plt.ylabel('Y-axis label')  # Replace with your desired label
plt.title('Plot of All Columns')  # Replace with your desired title
# Add legend for each column
plt.legend(blue_data.columns[1:] + red_data.columns[1:])
plt.show()
