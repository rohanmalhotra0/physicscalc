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
    
    def plot_velocity():
        time = np.linspace(0, t, 100)
        velocity = v0 + a * time
        plt.plot(time, velocity)
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.title("Velocity vs Time")
        plt.grid(True)
        plt.show()
    plot_velocity()
def calculate_distance():
    print("Distance Calculator")
    print("Enter the initial velocity (m/s):")
    v0 = float(input())
    print("Enter the time (s):")
    t = float(input())
    print("Enter the acceleration (m/s^2):")
    a = float(input())
    d = v0 * t + 0.5 * a * t**2
    print(f"The distance traveled is: {d} m")
    
    def plot_distance():
        time = np.linspace(0, t, 100)
        distance = v0 * time + 0.5 * a * time**2
        plt.plot(time, distance)
        plt.xlabel("Time (s)")
        plt.ylabel("Distance (m)")
        plt.title("Distance vs Time")
        plt.grid(True)
        plt.show()
    plot_distance()
def calculate_acceleration():
    print("Acceleration Calculator")
    print("Enter the initial velocity (m/s):")
    v0 = float(input())
    print("Enter the final velocity (m/s):")
    vf = float(input())
    print("Enter the time (s):")
    t = float(input())
    a = (vf - v0) / t
    print(f"The acceleration is: {a} m/s^2")
    
    def plot_acceleration():
        time = np.linspace(0, t, 100)
        acceleration = np.full_like(time, a)
        plt.plot(time, acceleration)
        plt.xlabel("Time (s)")
        plt.ylabel("Acceleration (m/s^2)")
        plt.title("Acceleration vs Time")
        plt.grid(True)
        plt.show()
    plot_acceleration()
def calculate_kinematics():
    print("Kinematics Calculator")
    print("Choose an option:")
    print("1. Projectile Motion")
    print("2. Final Velocity")
    print("3. Distance")
    print("4. Acceleration")
    choice = int(input())
    
    if choice == 1:
        calculate_projectile()
    elif choice == 2:
        calculate_final_velocity()
    elif choice == 3:
        calculate_distance()
    elif choice == 4:
        calculate_acceleration()
    else:
        print("Invalid choice.")

def calculate_electric_field():
    print("Electric Field Calculator")
    print("Choose a setting:")
    print("1. Lambda")
    print("2. Radius")
    print("3. Length")
    setting = input()
    
    if setting == "l":
        Lambda = float(input("What is the value of Lambda: "))
        Radius = float(input("Range of values for Radius 1-"))
        Length = float(input("What is the value of Length: "))
        
        xpoints = np.linspace(1, Lambda, num=int(Lambda))
        ypoints = np.zeros_like(xpoints)
        
        for i in range(len(xpoints)):  
            ypoints[i] = (1 / (4 * np.pi * sc.epsilon_0)) * (2 * xpoints[i] / Radius) / (
                np.sqrt(1 + (4 * Radius**2) / (Length**2))
            )
        
        plt.plot(xpoints, ypoints, 'o', label="Electric Field")
        plt.xlabel("Position along length")
        plt.ylabel("Electric Field (V/m)")
        plt.title("Electric Field Distribution")
        plt.legend()
        plt.grid()
        
        for i in range(len(xpoints)):
            print("Lambda Value:" + str(xpoints[i]))
            print("E Field Value:" + str(ypoints[i]))
        
        plt.show()
    elif setting == "r":
        Lambda = float(input("What is the value of Lambda: "))
        Radius = float(input("Range of values for Radius 1-"))
        Length = float(input("What is the value of Length: "))
        
        xpoints = np.linspace(1, Radius, num=int(Radius))
        ypoints = np.zeros_like(xpoints)
        
        for i in range(len(xpoints)):  
            ypoints[i] = (1 / (4 * np.pi * sc.epsilon_0)) * (2 * xpoints[i] / Radius) / (
                np.sqrt(1 + (4 * Radius**2) / (Length**2))
            )
        
        plt.plot(xpoints, ypoints, 'o', label="Electric Field")
        plt.xlabel("Position along length")
        plt.ylabel("Electric Field (V/m)")
        plt.title("Electric Field Distribution")
        plt.legend()
        plt.grid()
        
        for i in range(len(xpoints)):
            print("Radius Value:" + str(xpoints[i]))

        
    