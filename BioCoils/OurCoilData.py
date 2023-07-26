import numpy as np
import matplotlib.pyplot as plt

# the inductance of each coil is about 6mH.
# Coil 1 data
V1 = [0, 4.38, 6.05, 7.66, 9.38, 12.39, 15.21]
I1 = [0, 1.23, 1.71, 2.19, 2.64, 3.52, 4.3]

# Coil 2 data
V2 = [0, 2.20, 4.48, 7.2, 9.93, 11.43, 15.21]
I2 = [0, 0.63, 1.33, 2.13, 2.90, 3.32, 4.35]

# Plot the data for both coils
plt.plot(I1, V1, 'ro', label='Coil 1')
plt.plot(I2, V2, 'bo', label='Coil 2')

# Add linear fits
m1, b1 = np.polyfit(I1, V1, 1)
plt.plot(I1, np.polyval([m1, b1], I1), 'r')
m2, b2 = np.polyfit(I2, V2, 1)
plt.plot(I2, np.polyval([m2, b2], I2), 'b')

plt.title('Voltage vs Current')
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.legend()

# Print the resistance for each coil
R1 = m1
R2 = m2
plt.text(
    2.8, 15, f'R Coil 1: {R1:.2f} Ω', fontsize=10, ha='center', va='center')
plt.text(
    2.8, 14, f'R Coil 2: {R2:.2f} Ω', fontsize=10, ha='center', va='center')

plt.show()
