import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def bloch(spinor):
    # Sphere coordinates
    u = np.linspace(0, 2 * np.pi, 200)
    v = np.linspace(0, np.pi, 200)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the sphere
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.3, rstride=5, cstride=5, linewidth=0)

    # Axes lines
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)  # x-axis
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)  # y-axis
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)  # z-axis

    # Axis labels
    ax.text(1.1, 0, 0, r'$|+\rangle$', color='r')
    ax.text(-1.3, 0, 0, r'$|-\rangle$', color='r')
    ax.text(0, 1.1, 0, r'$|i\rangle$', color='g')
    ax.text(0, -1.3, 0, r'$|-i\rangle$', color='g')
    ax.text(0, 0, 1.1, r'$|0\rangle$', color='b')
    ax.text(0, 0, -1.3, r'$|1\rangle$', color='b')

    # Set limits and labels
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])
    ax.set_box_aspect([1,1,1])
    ax.axis('off')

    plt.tight_layout()
    plt.show()

def bloch_circle(state):
    fig, ax = plt.subplots()

    phi = np.linspace(0, 2*np.pi, 300)
    x = np.cos(phi)
    y = np.sin(phi)

    ax.set_aspect(1)

    #ax.quiver([0,0],[0,1])



    ax.quiver(0, 0,       # origin (x, y)
          0, 1,       # direction (u, v)
          angles='xy', scale_units='xy', scale=1, 
          color='r', width=0.01)
    
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    bloch_circle(1)