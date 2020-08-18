"""An example of reading topographical data from a file and displaying it."""

import pandas as pd
import matplotlib.pyplot as plt


topo_file = "../../data/boulder-topography.asc"


def read():
    try:
        topo = pd.read_csv(topo_file, header=None)
    except IOError:
        print("IOError: file '{}' cannot be read".format(topo_file))
    else:
        return topo


def display(data, show=False, outfile="boulder_dem.png"):
    fig, ax = plt.subplots()
    elev = ax.imshow(data, cmap="viridis")
    fig.colorbar(elev, label="Elevation (m)")
    plt.title("Boulder Topography")

    if show is True:
        plt.show()
    else:
        plt.savefig(outfile, dpi=96)
        plt.close()


if __name__ == "__main__":
    topo = read()
    if topo is not None:
        display(topo)
