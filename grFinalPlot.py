import numpy as np
import matplotlib.pyplot as plt


M = 2
a = 1.0

plot_singularity = True
plot_outer_horizon = True
plot_inner_horizon = True
plot_ergosphere = True


n_theta = 200
n_phi = 200

theta = np.linspace(0, np.pi, n_theta)
phi = np.linspace(0, 2*np.pi, n_phi)
theta, phi = np.meshgrid(theta, phi)



# Outer 
b = M + np.sqrt(M**2 - a**2)
# iner 
c = M - np.sqrt(M**2 - a**2)

# Ergosphere rho
rho = M + np.sqrt(M**2 - (a**2) * (np.cos(theta)**2))


def sph_to_cart(r, theta, phi):
    x = np.sqrt(r**2+a**2) * np.sin(theta) * np.cos(phi)
    y = np.sqrt(r**2+a**2) * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')


if plot_ergosphere:
    x, y, z = sph_to_cart(rho, theta, phi)
    ax.plot_surface(x, y, z, alpha=0.3, color='yellow', linewidth=0)


if plot_outer_horizon:
    r = b
    x, y, z = sph_to_cart(r, theta, phi)
    ax.plot_surface(x, y, z, alpha=0.4, color='orange', linewidth=0)


if plot_inner_horizon:
    r = c
    x, y, z = sph_to_cart(r, theta, phi)
    ax.plot_surface(x, y, z, alpha=0.4, color='red', linewidth=0)

if plot_singularity:
    phi_ring = np.linspace(0, 2*np.pi, 500)
    x = a * np.cos(phi_ring)
    y = a * np.sin(phi_ring)
    z = np.zeros_like(phi_ring)
    ax.plot(x, y, z, color='purple', linewidth=3)


ax.set_box_aspect([1,1,1])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Set limits for clarity
limit = 2*M
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])
ax.set_zlim([-limit, limit])

plt.title("Horizons, Ergosphere, Ring Singularity")
plt.show()