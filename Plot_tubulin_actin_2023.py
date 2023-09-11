import numpy as np
import matplotlib.pyplot as plt

# Bright pixel counts for Tubulin
tubulin_counts = [81124, 35965, 90579, 19633, 13763, 11703]

# Total areas inside Actin objects
actin_areas = [562886.0, 539848.0, 572895.0, 433665.5, 205596.0, 201333.0]

# Calculate the ratios for each pair
ratios = [tubulin_count / actin_area for tubulin_count,
          actin_area in zip(tubulin_counts, actin_areas)]

# Calculate the mean value and standard deviation
mean_ratio = np.mean(ratios)
std_dev = np.std(ratios)

# Calculate the standard deviation error
std_error = std_dev / np.sqrt(len(ratios))

# Print the results
print(f"Mean Ratio: {mean_ratio:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
print(f"Standard Deviation Error: {std_error:.4f}")

# Create a barplot
plt.bar(["Mean Ratio"], [mean_ratio], yerr=std_error, capsize=5)
plt.ylabel("Ratio")
plt.title("Mean Ratio of Bright Pixel Count to Total Area")
plt.show()
