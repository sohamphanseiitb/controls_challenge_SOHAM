# Controls Challenge - Solution Attempt by Soham

## Implementing a MPC controller

We have the following cost to minimize at the global scale:

- `lataccel_cost`: $\dfrac{\Sigma(actual\_lat\_accel - target\_lat\_accel)^2}{steps} \times 100$

- `jerk_cost`: $\dfrac{\Sigma((actual\_lat\_accel_t - actual\_lat\_accel_{t-1}) / \Delta t)^2}{steps - 1} \times 100$

Minimize: `total_cost`: $(lataccel\_cost \times 50) + jerk\_cost$

However, inside the controller, we have access 