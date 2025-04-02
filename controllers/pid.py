from . import BaseController
import numpy as np

class Controller(BaseController):
  """
  A simple PID controller
  """
  def __init__(self,):
    self.p = 0.3
    self.i = 0.05
    self.d = -0.1
    self.error_integral = 0
    self.prev_error = 0

# earlier we only used to get the latest values of target_lataccel and state
## now we are getting the whole history, and step_idx, which tells us which one to use:
  def update(self, target_lataccel, current_lataccel, state, step_idx, future_plan):
      
      error = (target_lataccel[step_idx] - current_lataccel)
      self.error_integral += error
      error_diff = error - self.prev_error
      self.prev_error = error
      return self.p * error + self.i * self.error_integral + self.d * error_diff
