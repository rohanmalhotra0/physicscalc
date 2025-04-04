import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

import scanner as sc # type: ignore

def calculate_projectile():
    print("projectile motion calculator")
    print("Enter the initial velocity (m/s):")
    v0 = float(input())
    print("Enter the launch angle (degrees):")
    theta = float(input())
    print("Enter the time of flight (s):")
    t = float(input())
    g = 9.81  # Acceleration due to gravity (m/s^2)
    # Convert angle to radians
    theta_rad = np.deg2rad(theta)
    # Calculate x and y positions
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    # Plot the trajectory
    plt.plot(x, y)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.title("Projectile Motion Trajectory")
    plt.grid(True)
    plt.show()

def calculate_final_velocity():
    print("Final Velocity Calculator")
    print("Enter the initial velocity (m/s):")
    v0 = float(input())
    print("Enter the acceleration (m/s^2):")
    a = float(input())
    print("Enter the time (s):")
    t = float(input())
    v = v0 + a * t
    print(f"The final velocity is: {v} m/s")
    