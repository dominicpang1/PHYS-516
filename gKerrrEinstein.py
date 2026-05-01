import numpy as np
from astropy import units as u
from einsteinpy.geodesic import Timelike
from einsteinpy.plotting import StaticGeodesicPlotter

mass = 2
position = [10.0, np.pi/2, 0]   # r, theta, phi
velocity = [0, 0, 5] 
end_lambda = 0.001
step_size = 5e-8

# Calculate the geodesic
geod = Timelike(
    metric="Kerr",
    metric_params =  (2),
    position=position,
    momentum=velocity,
    steps=1000,
    delta=step_size,
    mass=mass
)
# Create a plotter instance
sgpl = StaticGeodesicPlotter()

# Add the calculated geodesic to the plot
sgpl.plot(geod, color="red")

# Display the plot
sgpl.show()