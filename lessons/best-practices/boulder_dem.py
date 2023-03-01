"""An example of reading topographical data from a file and displaying it."""

import matplotlib.pyplot as plt
import pandas as pd

topo_file = "../../data/topo.asc"


def read():
    try:
        topo = pd.read_csv(topo_file, header=None)
    except OSError:
        print(f"IOError: file {topo_file!r} cannot be read")
    else:
        return topo


def display(data, show=False, outfile="boulder_dem.png"):
    fig, ax = plt.subplots()
    elev = ax.imshow(data, cmap="jet")
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
