
import numpy as np
import matplotlib.pyplot as plt

# Measurement values
measurements = [(-62, 29, -122), (-61, 38, -193), (-61, 46, -221),
                (-58, 46, -227), (-64, 48, -217), (-62, 50, -183), (-56, 57, -148)]

# Offset values
offset = (-65, 41, 22)

# Function to reduce offset from the measurement values


def reduce_offset(measurement, offset):
    return tuple(val - offset_val for val, offset_val in zip(measurement, offset))


# Reduce offset from each measurement
reduced_measurements = [reduce_offset(
    measurement, offset) for measurement in measurements]

# Extract the individual components (Bx, By, Bz) after offset reduction
Bx_values = [measurement[0] for measurement in reduced_measurements]
By_values = [measurement[1] for measurement in reduced_measurements]
Bz_values = [measurement[2] for measurement in reduced_measurements]

# Corresponding coordinates in mm
r = np.array([-56.4, -38, -19, 0, 19, 38, 56.4])

# Fit a 2nd-degree polynomial to Bz_values (quadratic fit)
fit_coeffs = np.polyfit(r, Bz_values, deg=2)
fit_function = np.poly1d(fit_coeffs)

# Generate more points for smoother curve
r_fit = np.linspace(np.min(r), np.max(r), 100)
fit_values = fit_function(r_fit)

# Create the subplots, one for Bx, By, and Bz, and another for Bz with the quadratic fit
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Left plot: Bx, By, and Bz
ax1.scatter(r, Bx_values, label='Bx', color='red')
ax1.plot(r, Bx_values, color='red', linestyle='--')
ax1.scatter(r, By_values, label='By', color='green')
ax1.plot(r, By_values, color='green', linestyle='--')
ax1.scatter(r, Bz_values, label='Bz', color='blue')
ax1.plot(r, Bz_values, color='blue', linestyle='--')
ax1.set_xlabel('Position [mm]')
ax1.set_ylabel('B [µT]')
ax1.set_title(
    'Bx, By, and Bz after offset reduction (Bx0=-65, By0=41, Bz0=22) µT')
ax1.legend()
ax1.grid(True)

# Right plot: Bz with the fitted quadratic curve
ax2.scatter(r, Bz_values, label='Bz', color='blue')
ax2.plot(r_fit, fit_values, color='purple',
         linestyle='-', label='Bz Fit (Quadratic)')
ax2.axvspan(-35 / 2, 35 / 2, facecolor='pink', alpha=0.3)
ax2.set_xlabel('Position [mm]')
ax2.set_ylabel('Bz [µT]')
ax2.set_title('Bz with fitted quadratic curve (Bz0=22) µT')

# Print the fit function as a text annotation inside the right plot
equation_text = f'$Bz = {fit_coeffs[0]:.2f}r^2 + {fit_coeffs[1]:.2f}r + {fit_coeffs[2]:.2f}$'
ax2.text(-40, -180, equation_text, fontsize=12, color='purple')

ax2.legend()
ax2.grid(True)

plt.tight_layout()

# Save the figure to a file (e.g., "output_plot.png")
plt.savefig("output_plot.png")

# Show the plot on the screen
plt.show()
