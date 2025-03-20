import numpy as np
import pandas as pd

data = pd.read_csv("")

class Kalman:
  def init(self,acceleration,pressure,orientation,velocity):
    self.acceleration = acceleration
    self.pressure = pressure
    self.orientation = orientation
    self.velocity = velocity
    return(acceleration,pressure,orientation,velocity)
  
  def estimate(estimate,obs_val,time):
    time = np.len(data)
    
    return
    