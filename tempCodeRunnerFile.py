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

# Plot the adjusted Bx, By, Bz values with scatter plots and connecting lines
plt.figure(figsize=(10, 6))
plt.scatter(r, Bx_values, label='Bx', color='red')
plt.plot(r, Bx_values, color='red', linestyle='--')
plt.scatter(r, By_values, label='By', color='green')
plt.plot(r, By_values, color='green', linestyle='--')
plt.scatter(r, Bz_values, label='Bz', color='blue')
plt.plot(r, Bz_values, color='blue', linestyle='--')

# Plot the fitted function as a scatter plot
plt.scatter(r, fit_function(r), label='Bz Fit', color='purple', marker='x')

# Plot the fit function as a smooth curve
# Generate more points for smoother curve
r_fit = np.linspace(np.min(r), np.max(r), 100)
plt.plot(r_fit, fit_function(r_fit), color='purple',
         linestyle='-', label='Bz Fit ')

# Add the pink rectangle
plt.axvspan(-35 / 2, 35 / 2, facecolor='pink', alpha=0.3)

# Print the fit function as a text annotation inside the plot
equation_text = f'$Bz = {fit_coeffs[0]:.2f}r^2 + {fit_coeffs[1]:.2f}r + {fit_coeffs[2]:.2f}$'
plt.text(-40, -180, equation_text, fontsize=12, color='purple')

plt.xlabel('Position [mm]')
plt.ylabel('Bi [µT]')
plt.title('Bi after offset reduction (Bx0=-65, By0=41, Bz0=22) µT')
plt.legend()
plt.grid(True)
plt.show()
