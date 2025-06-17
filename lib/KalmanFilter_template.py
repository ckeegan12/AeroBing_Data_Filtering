# AeroBing Kalman Filter template(creator: Cian Keegan)
# Kalman Filter for smooth out data graph to be able to obtain an accurate derivative
import numpy as np
import pandas as pd

# import data here

# Initialization
R = 0.1 # measurement of covariance (can be changed)
C = 0.002 # process of covariance (can be changed)

x = np.zeros(num_measurements)        # Current measurement
p = np.zeros(num_measurements)        # Current error term
x_minus = np.zeros(num_measurements)  # Past measurement
p_minus = np.zeros(num_measurements)  # Past error term
k_gain = np.zeros(num_measurements)   # Kalman gain

x[0] = 0
p[0] = 1

# Updating variables loop
for i in range(1,num_measurement):
    x_minus[i] = x[i-1]
    p_minus[i] = p[i-1] + C

    k_gain[i] = p_minus[i] / (p_minus[i]+R) 
    x[i] = x_minus[i] + k_gain[i] * (measurement[i] - x_minus[i])
    p[i] = (1-k_gain[i]) * p_minus[i]

# plot x to see new smoothed dataset
