import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Input for initial velocity and launch angle
while True:
    try:
        v0 = float(input("Enter the initial velocity (m/s): "))  # Initial velocity (m/s)
        if v0 <= 0:
            raise ValueError("Velocity must be greater than 0.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a positive number.")

while True:
    try:
        theta = float(input("Enter the launch angle (degrees): "))  # Launch angle (degrees)
        if not 0 <= theta <= 180:
            raise ValueError("Angle must be between 0 and 180 degrees.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid angle.")

# Input for time settings
while True:
    try:
        total_time = float(input("Enter the total simulation time (seconds): "))  # Total time for simulation
        if total_time <= 0:
            raise ValueError("Time must be greater than 0.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a positive number.")

while True:
    try:
        time_steps = int(input("Enter the number of time steps: "))  # Number of time steps
        if time_steps <= 0:
            raise ValueError("Number of steps must be greater than 0.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a positive integer.")

# Time array
t = np.linspace(0, total_time, time_steps)

# Equations of motion
x = v0 * np.cos(np.radians(theta)) * t  # Horizontal displacement
y = v0 * np.sin(np.radians(theta)) * t - 0.5 * g * t**2  # Vertical displacement

# Filter for points above ground (y >= 0)
x = x[y >= 0]
y = y[y >= 0]

# Plot trajectory
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f"v₀ = {v0} m/s, θ = {theta}°")
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.legend()
plt.show()
