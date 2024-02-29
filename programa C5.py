import matplotlib.pyplot as plt
import numpy as np

def plot_C(ax):
    x = np.linspace(0, 1, 100)
    y_top = np.sqrt(1 - (x-0.5)**2)
    y_bottom = -np.sqrt(1 - (x-0.5)**2)
    ax.plot(x, y_top, 'k')
    ax.plot(x, y_bottom, 'k')

def plot_A(ax):
    ax.plot([0, 0.5, 1], [0, 1, 0], 'k')
    ax.plot([0.25, 0.5, 0.75], [0.5, 1, 0.5], 'k')

def plot_M(ax):
    ax.plot([0, 0.5, 1, 1.5, 2], [0, 1, 0, 1, 0], 'k')

def plot_I(ax):
    ax.plot([0.5, 0.5], [0, 1], 'k')

def plot_L(ax):
    ax.plot([1, 1], [0, 1], 'k')
    ax.plot([1, 2], [0, 0], 'k')

def plot_O(ax):
    circle = plt.Circle((2.5, 0.5), 0.5, color='k', fill=False)
    ax.add_artist(circle)

fig, ax = plt.subplots(figsize=(6, 3))

plot_C(ax)
plot_A(ax)
plot_M(ax)
plot_I(ax)
plot_L(ax)
plot_O(ax)

# Ajustes de los límites del gráfico
ax.set_xlim(0, 3)
ax.set_ylim(0, 1)

# Eliminar ejes
ax.axis('off')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()
