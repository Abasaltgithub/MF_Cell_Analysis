
# I meausred the MF of the old coil at HH confuigfuration ruuning at I=0.11A (1.2V) using sesnor LIS3MDL


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

# Plot the adjusted Bx, By, Bz values with scatter plots and connecting lines
plt.figure(figsize=(10, 6))
plt.scatter(r, Bx_values, label='Bx', color='red')
plt.plot(r, Bx_values, color='red', linestyle='--')
plt.scatter(r, By_values, label='By', color='green')
plt.plot(r, By_values, color='green', linestyle='--')
plt.scatter(r, Bz_values, label='Bz', color='blue')
plt.plot(r, Bz_values, color='blue', linestyle='--')

# Add the pink rectangle
plt.axvspan(-35 / 2, 35 / 2, facecolor='pink', alpha=0.3)

plt.xlabel('Position [mm]')
plt.ylabel('Bi [µT]')
plt.title('Bi after offset reduction (Bx0=-65, By0=41, Bz0=22) µT')
plt.legend()
plt.grid(True)
plt.show()
