import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
a = 0.9
M = 1.5
# ergoregion = 2 
mu = 0
r_0 = 10
theta_0 = np.pi/3 #equatorial plane
p_theta_0 = 0
E = 0.95
Phi =  3 # initial azimuthal angular momentum

# functions
def K_ini(theta_ini,p_theta_ini):
    return p_theta_ini**2 + (a*E*np.sin(theta_ini)-Phi/np.sin(theta_ini))**2
def Q_ini(K_ini):
    return K_ini-(Phi-a*E)**2
K = K_ini(theta_0,p_theta_0)
Q = Q_ini(K)

def fancyTheta(theta,Q,a,mu,E,Phi):
    return Q-np.cos(theta)**2 * (a**2*(mu**2 - E**2) + (Phi**2)/(np.sin(theta)**2))
def P(r,a,E,Phi):
    return E*(r**2+a**2)-Phi*a
def R(r,M,a,mu,K,E,Phi):
    P_val = P(r,a,E,Phi)
    delta = r**2-2*M*a+a**2
    return P_val**2 - delta*(mu**2*r**2 + K)

# diff eqs
def thetadot(r,theta,Q,a,mu,E,Phi):
    rho_squared = r**2+a**2*np.cos(theta)**2
    return np.sqrt(fancyTheta(theta,Q,a,mu,E,Phi))*(rho_squared)**-1

def rdot(r,theta,P,M,a,mu,K):
    rho_squared = r**2+a**2*np.cos(theta)**2
    return np.sqrt(R(P,r,M,a,mu,K)) * (rho_squared)**-1

def phidot(r,theta,a,M,mu,E,Phi,K):
    rho2 = r**2 + a**2*np.cos(theta)**2
    delta = r**2 - 2*M*r + a**2
    P_val = P(r,a,E,Phi)
    R_val = R(r,M,a,mu,K,E,Phi)
    
    return (1/rho2)*(
        -(a*E - Phi/(np.sin(theta)**2))
        + (a/delta)*(np.sqrt(R_val) - P_val)
    )
sign_r = 0     # choose initial direction (inward or outward)
sign_theta = 1   # usually fine if starting at equator

tol = 1e-8

def geodesic(lam, y):
    global sign_r, sign_theta
    
    r, theta, phi = y
    
    rho2 = r**2 + a**2 * np.cos(theta)**2
    
    # Compute potentials
    R_val = R(r, M, a, mu, K, E, Phi)
    
    Theta_val = fancyTheta(theta, Q, a, mu, E, Phi)
    
    # 
    # if R_val < 0:
    #     R_val = 0
    # if Theta_val < 0:
    #     Theta_val = 0
    
    if R_val < tol:
        sign_r *= -1
    
    if Theta_val < tol:
        sign_theta *= -1
    
    dr = sign_r * np.sqrt(R_val) / rho2
    dtheta = sign_theta * np.sqrt(Theta_val) / rho2
    dphi = phidot(r, theta, a, M, mu, E, Phi, K)
    
    return [dr, dtheta, dphi]

from scipy.integrate import solve_ivp

y0 = [r_0, theta_0, 0]

if R(r_0, M, a, mu, K, E, Phi) < 0:
    raise ValueError("Invalid initial conditions: R < 0")

sol = solve_ivp(
    geodesic,
    t_span=(0, 1000),
    y0=y0,
    method='RK45',
    max_step=0.05
)


# plotting time 

# Extract solution
r = sol.y[0]
theta = sol.y[1]
phi = sol.y[2]

# Convert to Cartesian-like coordinates
x = np.sqrt(r**2 + a**2) * np.sin(theta) * np.cos(phi)
y = np.sqrt(r**2 + a**2) * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Create 3D plot
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

# Plot trajectory
ax.plot(x, y, z, linewidth=1.5)

# Mark starting point
ax.scatter(x[0], y[0], z[0], color='green', label='start')

# Mark ending point
ax.scatter(x[-1], y[-1], z[-1], color='red', label='end')



ax.set_title("Kerr Photon Trajectory")

ax.legend()

# Equal aspect ratio
max_range = np.array([
    x.max()-x.min(),
    y.max()-y.min(),
    z.max()-z.min()
]).max() / 2.0

mid_x = (x.max()+x.min()) * 0.5
mid_y = (y.max()+y.min()) * 0.5
mid_z = (z.max()+z.min()) * 0.5

# Set limits for clarity
limit = 10*M
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])
ax.set_zlim([-limit, limit])

def plotBlackHole(plot_ergosphere,plot_outer_horizon,plot_inner_horizon,plot_singularity):
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
plotBlackHole(True,True,True,True)
plt.show()
