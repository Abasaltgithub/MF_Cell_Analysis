import matplotlib.pyplot as plt
import numpy as np

# Data
I = [0.378, 0.763, 1.181, 1.817, 2.274, 2.846,
     3.629, 4.158, 4.625, 4.973, 5.699, 6.555]
V = [1.49, 3.07, 4.71, 7.29, 9.12, 11.47,
     14.68, 16.95, 19.02, 20.68, 23.99, 28.24]
Bx = [-0.081, -0.097, -0.252, -0.294, -0.418, -0.4431, -
      0.552, -0.622, -0.643, -0.331, -0.442, -0.747]
By = [-0.147, -0.142, -0.243, -0.374, -0.430, -0.540, -
      0.620, -0.658, -0.719, -0.623, -0.981, -1.069]
Bz = [1.181, 2.333, 3.495, 4.979, 6.099, 7.630,
      10.13, 11.52, 12.78, 13.73, 15.99, 18.24]

# Linear fit function


def plot_linear_fit(ax, x, y, xlabel, ylabel, title):
    coeffs = np.polyfit(x, y, 1)  # Calculate best-fit line coefficients
    # Generate line coordinates using the coefficients
    line = np.polyval(coeffs, x)

    ax.plot(x, y, 'o')
    ax.plot(x, line, color='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)


# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(11, 4))

# Plot V versus I with linear fit
axs[0].plot(I, V, 'o', color='blue')
coeffs = np.polyfit(I, V, 1)
line = np.polyval(coeffs, I)
axs[0].plot(I, line, color='black', label='Linear Fit')
axs[0].set_xlabel('Current (A)')
axs[0].set_ylabel('Voltage (V)')
axs[0].set_title('Voltage vs. current')
equation = f'V = {coeffs[0]:.3f} x I + {coeffs[1]:.3f}'
axs[0].text(0.1, 0.9, equation, transform=axs[0].transAxes)

# Plot I versus Bx, By, and Bz with linear fits
axs[1].plot(I, Bx, 'o', color='orange', label="Bx")
axs[1].plot(I, By, 'o', color='blue', label="By")
axs[1].plot(I, Bz, 'o', color='green', label="Bz")
plot_linear_fit(axs[1], I, Bx, 'Current (A)', 'Bx (mT)', 'Current versus Bx')
plot_linear_fit(axs[1], I, By, 'Current (A)', 'By (mT)', 'Current versus By')
plot_linear_fit(axs[1], I, Bz, 'Current (A)', 'Bz (mT)', 'Current versus Bz')
axs[1].set_xlabel('Current (A)')
axs[1].set_ylabel('Magnetic Field (mT)')
axs[1].set_title('Current vs. Bx, By, and Bz')

# Linear fit function Bz
coeffs = np.polyfit(I, Bz, 1)  # Calculate best-fit line coefficients
equation2 = f'Bz = {coeffs[0]:.3f} x I + {coeffs[1]:.3f}'
axs[1].text(1.2, 0.6, equation2, transform=axs[0].transAxes)
axs[1].legend(loc='upper left')

# Adjust subplot spacing
plt.tight_layout()
plt.savefig('I_V_Bx_By_Bz.png')
plt.show()


#  plotting linear fits of I versus Bx, By, Bz
variables = ['Bx', 'By', 'Bz']
equations = []
for variable in variables:
    coeffs = np.polyfit(I, eval(variable), 1)
    equation = f'{variable} = {coeffs[0]:.3f} x I + {coeffs[1]:.3f}'
    equations.append(equation)

# Print the linear fit equations
for i, equation in enumerate(equations):
    print(f"Linear Fit Equation for I versus {variables[i]}:")
    print(equation)
    print()
