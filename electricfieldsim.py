import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.arange(-10, 10, 0.5), np.arange(-10, 10, 0.5))

x_fine, y_fine = np.meshgrid(np.arange(-10, 10, 0.025), np.arange(-10, 10, 0.025))

Charges = np.array([[1,-3,0], 
                   [-1,3,0],
                   ])  # Charge, x position, y position

fx = np.zeros_like(x)
fy = np.zeros_like(y)

fx_fine = np.zeros_like(x_fine)
fy_fine = np.zeros_like(y_fine)


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
    fx_fine += q * dx_fine / r_fine**3
    fy_fine += q * dy_fine / r_fine**3

magnitude = np.sqrt(fx**2 + fy**2) #normalizing arrows
magnitude_fine = np.sqrt(fx_fine**2 + fy_fine**2) #normalizing arrows

fx /= magnitude
fy /= magnitude

fx_fine_n = fx_fine / magnitude_fine
fy_fine_n = fy_fine / magnitude_fine

###

def divergence(x,y,fx,fy):
    return np.gradient(fx, axis=1) + np.gradient(fy, axis=0)


div = divergence(x_fine, y_fine, fx_fine_n, fy_fine_n)
div_log = np.sign(div) * np.log1p(np.abs(div))
vmax = np.percentile(div_log, 99.9)
vmin = np.percentile(div_log, 0.1)
div_log = np.clip(div_log, vmin, vmax)


plt.figure(figsize=(10,10))
plt.imshow(div_log, extent=[x_fine.min(), x_fine.max(), y_fine.min(), y_fine.max()], origin='lower', cmap='coolwarm', alpha=0.7, vmin=vmin, vmax=vmax)
plt.quiver(x, y, fx, fy, magnitude, cmap='inferno', scale=50)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title(' Vector Field')
plt.show()