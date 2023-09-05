import matplotlib.pyplot as plt
import numpy as np

# Create the current_A and B_mT lists
current_A = [0.205, 0.44, 0.799, 1.12, 1.51, 1.73, 2.2, 2.32, 2.71, 2.99, 3.4]
current_A = np.array(current_A)
B_mT = [0.88, 1.92, 3.49, 4.89, 6.61, 7.57, 8.98, 10.11, 11.8, 13.0, 14.75]

# simulation for radius = 43mm, N=210, from https://tiggerntatie.github.io/emagnet/offaxis/iloopcalculator.htm
B_mT_sim = [0.88, 1.87, 3.41, 4.78, 6.44,
            7.38, 9.39, 9.90, 11.56, 12.78, 14.51]

# Define error bars
errors = [0.05 * B for B in B_mT]

# Create a scatter plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# First subplot for the magnetic field plot
ax1.scatter(current_A, B_mT, c='black', label='Measurement', zorder=2)
ax1.errorbar(current_A, B_mT, yerr=errors, fmt='none',
             c='black', capsize=3, zorder=1)
ax1.plot(current_A, B_mT_sim, c='blue', label='Simulation for R=43mm, N=210')
ax1.set_xlabel('Current (A)')
ax1.set_ylabel('Axial Magnetic Field (mT)')
ax1.set_title('Current vs. magnetic field of the BioCoil')

# Perform a linear fit using numpy's polyfit function
m, b = np.polyfit(current_A, B_mT, 1)
ax1.plot(current_A, m*current_A + b, color='red',
         label='Linear fit to measurement')
ax1.text(0.4, 10, f'B(mT) = {m:.2f} x I (A) + {b:.2f}',
         fontsize=10, color='red')

ax1.legend()

# Second subplot for the I-V plot
current = [0.262, 0.392, 0.62, 0.807, 1.13, 1.48, 2.08, 2.5, 4.47]
voltage = [1.57, 2.36, 3.82, 4.96, 6.96, 9.16, 12.93, 15.64, 28.17]

# linear fit
slope, intercept = np.polyfit(current, voltage, 1)
x = np.array(current)
y = slope * x + intercept

# scatter plot
ax2.scatter(current, voltage, label='Measurement', c='black')
ax2.plot(x, y, label='Linear Fit', color='r')

# add labels and legend
ax2.set_title('Voltage vs. Current')
ax2.set_xlabel('Current (A)')
ax2.set_ylabel('Voltage (V)')
ax2.legend()

# add text box with equation of line
equation = f'V = {slope:.2f} x I + {intercept:.2f}'
ax2.text(2.5, 10, equation, fontsize=12, c='red')

plt.tight_layout()

output_image_path = 'MagneticFieldSimulation.pdf'
plt.savefig(output_image_path, bbox_inches='tight',
            dpi=500)  # Save with specified DPI

output_path = '/Users/abasaltbahrami/Downloads/AxialField_measured.pdf'
plt.savefig(output_path, format='pdf')

plt.show()
