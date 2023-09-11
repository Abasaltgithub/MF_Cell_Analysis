import numpy as np
import matplotlib.pyplot as plt

# Bright pixel counts for Tubulin in CTR and MF
tubulin_counts_ctr = [162187, 153373, 44080, 200729, 187739, 154226]
tubulin_counts_mf = [81124, 35965, 90579, 19633, 13763, 11703]

# Total areas inside Actin objects for CTR and MF
actin_areas_ctr = [336796.0, 412579.0, 699813.5, 640681.0, 443439.5, 286664.0]
actin_areas_mf = [562886.0, 539848.0, 572895.0, 433665.5, 205596.0, 201333.0]

# Calculate the ratios for each pair in CTR and MF
ratios_ctr = [tubulin_count / actin_area for tubulin_count,
              actin_area in zip(tubulin_counts_ctr, actin_areas_ctr)]
ratios_mf = [tubulin_count / actin_area for tubulin_count,
             actin_area in zip(tubulin_counts_mf, actin_areas_mf)]

# Calculate the mean value and standard deviation for CTR and MF
mean_ratio_ctr = np.mean(ratios_ctr)
std_dev_ctr = np.std(ratios_ctr)
mean_ratio_mf = np.mean(ratios_mf)
std_dev_mf = np.std(ratios_mf)

# Calculate the standard deviation error for CTR and MF
std_error_ctr = std_dev_ctr / np.sqrt(len(ratios_ctr))
std_error_mf = std_dev_mf / np.sqrt(len(ratios_mf))

# Print the results for CTR and MF
print("CTR Data:")
print(f"Mean Ratio: {mean_ratio_ctr:.4f}")
print(f"Standard Deviation: {std_dev_ctr:.4f}")
print(f"Standard Deviation Error: {std_error_ctr:.4f}")

print("MF Data:")
print(f"Mean Ratio: {mean_ratio_mf:.4f}")
print(f"Standard Deviation: {std_dev_mf:.4f}")
print(f"Standard Deviation Error: {std_error_mf:.4f}")

# Create a barplot for CTR and MF
plt.bar(["Mean Ratio (CTR)", "Mean Ratio (MF)"],
        [mean_ratio_ctr, mean_ratio_mf],
        yerr=[std_error_ctr, std_error_mf],
        capsize=5)
plt.ylabel("Ratio")
plt.title("Mean Ratio of Bright Pixel Count to Total Area")
plt.show()
