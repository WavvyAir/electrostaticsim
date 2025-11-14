import numpy as np
import matplotlib.pyplot as plt



x, y = np.meshgrid(np.arange(-10, 10, 0.5), np.arange(-10, 10, 0.5))

x_fine, y_fine = np.meshgrid(np.arange(-10, 10, 0.025), np.arange(-10, 10, 0.025))

Charges = np.array([[1,-3,0],
                   [-1,3,0],
                   [1,0,3],
                   [-1,0,-3]])  # Charge, x position, y position

fx = np.zeros_like(x)
fy = np.zeros_like(y)

fx_fine = np.zeros_like(x_fine)
fy_fine = np.zeros_like(y_fine)

U= np.zeros_like(x_fine)

for q, x0, y0 in Charges:

    dx = x - x0
    dy = y - y0
    r = np.sqrt(dx**2 + dy**2)
    r[r == 0] = 1e-10  # Avoid division by zero
    fx += q * dx / r**3
    fy += q * dy / r**3

    dx_fine = x_fine - x0
    dy_fine = y_fine - y0
    r_fine = np.sqrt(dx_fine**2 + dy_fine**2)
    r_fine[r_fine == 0] = 1e-10
    U += q / r_fine

magnitude = np.sqrt(fx**2 + fy**2)

#normalizing arrows
fx /= magnitude
fy /= magnitude


###
magnitude_log = np.sign(magnitude) * np.log1p(10*np.abs(magnitude))
U_log = np.sign(U) * np.log1p(np.abs(U))

vmax = np.percentile(U_log, 99.9)
vmin = np.percentile(U_log, 0.1)


plt.figure(figsize=(10,10))
plt.imshow(U, extent=[x_fine.min(), x_fine.max(), y_fine.min(), y_fine.max()], origin='lower', cmap='coolwarm', alpha=0.7, vmin=vmin, vmax=vmax)
plt.quiver(x, y, fx, fy, magnitude_log, cmap='inferno', scale=50)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title('Electric Field')
plt.show()
