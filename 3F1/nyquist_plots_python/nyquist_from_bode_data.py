import numpy as np
import matplotlib.pyplot as plt
import json
import math

with open(r'./data/gain.json') as f:
    gain_dict = json.load(f)
    
with open(r'./data/phase.json') as f:
    phase_dict = json.load(f)


gain_db = np.array(gain_dict["data"])
gain = 10**(gain_db/10)
phase_degrees = np.array(phase_dict["data"])
phase_rad = phase_degrees * math.pi / 180

def polar_to_car(r_array, theta_array):
    return np.cos(theta_array) * r_array, np.sin(theta_array) * r_array


x_array, y_array = polar_to_car(gain, phase_rad)

print(phase_rad/(math.pi*2))
print(gain)


# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x_array, y_array)
plt.show() 