import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sc


setting = input("What value is variable r, l, Lambda(x):")

if setting == "x":
    Lambda = float(input("Value range of lambda 1-"))
    Radius = float(input("What is the value of radius: "))
    Length = float(input("What is the value of length: "))
    xpoints = np.linspace(1, Lambda, num=int(Lambda))
    ypoints = np.zeros_like(xpoints)

    for i in range(len(xpoints)):  
        ypoints[i] = (1 / (4 * math.pi * sc.epsilon_0)) * (2 * xpoints[i] / Radius) / (
            math.sqrt(1 + (4 * Radius**2) / (Length**2))
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
    Lambda = float(input("What is the value of Lambda:"))
    Radius = float(input("Range of values for Radius 1-"))
    Length = float(input("What is the value of Length: "))

    xpoints = np.linspace(1, Radius, num=int(Radius))
    ypoints = np.zeros_like(xpoints)

    for i in range(len(xpoints)):  
        ypoints[i] = (1 / (4 * math.pi * sc.epsilon_0)) * (2 * xpoints[i] / Radius) / (
            math.sqrt(1 + (4 * Radius**2) / (Length**2))
        )

    plt.plot(xpoints, ypoints, 'o', label="Electric Field")
    plt.xlabel("Position along length")
    plt.ylabel("Electric Field (V/m)")
    plt.title("Electric Field Distribution")
    plt.legend()
    plt.grid()

    for i in range(len(xpoints)):
        print("Radius Value:" + str(xpoints[i]))
        print("E Field Value:" + str(ypoints[i]))

    plt.show()
elif setting == "l":
    Lambda = float(input("What is the value of Lambda:"))
    Radius = float(input("What is the value of Range:"))
    Length = float(input("Value range of Length 1-"))

    xpoints = np.linspace(1, Length, num=int(Length))
    ypoints = np.zeros_like(xpoints)

    for i in range(len(xpoints)):  
        ypoints[i] = (1 / (4 * math.pi * sc.epsilon_0)) * (2 * xpoints[i] / Radius) / (
            math.sqrt(1 + (4 * Radius**2) / (Length**2))
        )

    plt.plot(xpoints, ypoints, 'o', label="Electric Field")
    plt.xlabel("Position along length")
    plt.ylabel("Electric Field (V/m)")
    plt.title("Electric Field Distribution")
    plt.legend()
    plt.grid()

    for i in range(len(xpoints)):
        print("Length Value:" + str(xpoints[i]))
        print("E Field Value:" + str(ypoints[i]))

    plt.show()