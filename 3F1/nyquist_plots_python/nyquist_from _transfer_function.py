import numpy as np
import matplotlib.pyplot as plt
import control


G = control.tf([2], [0.5, -1]) # Part 5
# G = control.tf([10],[1, 10, 0]) # Part 1


print(G)

# to add time delay
(num,den) = control.pade(0.25,3)
print(num,den)
Gp = control.tf(num,den)*G
print(Gp)

# mag,phase,omega = control.bode(G)
output = control.nyquist_plot(Gp)
plt.show()
