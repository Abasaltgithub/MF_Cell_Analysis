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

# Print ratios_ctr and ratios_mf
print("CTR Ratios:")
print(ratios_ctr)

print("\nMF Ratios:")
print(ratios_mf)

# Calculate the mean value and standard deviation for CTR and MF
mean_ratio_ctr = np.mean(ratios_ctr)
std_dev_ctr = np.std(ratios_ctr)
mean_ratio_mf = np.mean(ratios_mf)
std_dev_mf = np.std(ratios_mf)

# Calculate the standard deviation error for CTR and MF
std_error_ctr = std_dev_ctr / np.sqrt(len(ratios_ctr))
std_error_mf = std_dev_mf / np.sqrt(len(ratios_mf))

# Print the labels for CTR and MF data only once
print("\nCTR Data:")
print(f"Mean Ratio: {mean_ratio_ctr:.4f}")
print(f"Standard Deviation: {std_dev_ctr:.4f}")
print(f"Standard Deviation Error: {std_error_ctr:.4f}")

print("\nMF Data:")
print(f"Mean Ratio: {mean_ratio_mf:.4f}")
print(f"Standard Deviation: {std_dev_mf:.4f}")
print(f"Standard Deviation Error: {std_error_mf:.4f}")

# Create a barplot for CTR and MF
plt.figure(figsize=(5, 5))

# Create bar plots for ratios_ctr and ratios_mf with error bars
bar_positions = (0.2, 0.3)
bar_width = 0.05

# Plot bars for CTR and MF
plt.bar(bar_positions, [mean_ratio_ctr, mean_ratio_mf], bar_width, yerr=[std_error_ctr, std_error_mf],
        capsize=5, color=['blue', 'orange'])

# Scatter plot for individual data points in CTR and MF
for i, ratio in enumerate(ratios_ctr):
    # Change marker to 'o' for circle
    plt.scatter(bar_positions[0], ratio, color='black',
                zorder=3, marker='o', label='Control' if i == 0 else '')

for i, ratio in enumerate(ratios_mf):
    # Change marker to '^' for triangle
    plt.scatter(bar_positions[1], ratio, color='black',
                zorder=3, marker='^', label='MF = 480$\mu$T' if i == 0 else '')

plt.legend()
plt.ylabel("Tubulin/ Actin Area")
plt.title(
    "Tubulin/Actin Ratios Following a 2H Nocodazole Treatment in A7R5 Cells", size=8)
plt.xticks(bar_positions, ["Control", "MF"])
plt.show()
