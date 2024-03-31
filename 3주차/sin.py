import matplotlib.pyplot as tae
import numpy as n

x = n.linspace(0, 2 * n.pi, 200)
y = n.sin(x)

fig, ax = tae.subplots()
ax.plot(x, y)
tae.show()