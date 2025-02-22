import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_structure(structure, title="Protein Structure"):
    """
    Visualizes the 3D structure of the protein.

    Args:
      structure: The 3D structure of the protein, represented as a list of
                 (x, y, z) coordinates for each atom.
      title: The title of the plot.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract x, y, and z coordinates from the structure
    x_coords = [atom for atom in structure]
    y_coords = [atom for atom in structure]
    z_coords = [atom for atom in structure]

    # Plot the atoms
    ax.scatter(x_coords, y_coords, z_coords)

    # Set plot title and labels
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
