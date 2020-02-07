import numpy as np


#!rdfstart!#
def rdf(bin_edges, r, V):
    """
    bin_edges = edges of bins. Typically np.linspace(0, rc, num_bins+1)
                for some cut-off rc.
    r = Nx3-array of positions of atoms at a given timestep.
    V = volume of system.
    """

    N = r.shape[0]

    bin_centres = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    bin_sizes = bin_edges[1:] - bin_edges[:-1]

    n = np.zeros_like(bin_sizes)

    for i in range(N):
        dr = np.linalg.norm(r - r[i], axis=1)     # Distances from atom i.
        n += np.histogram(dr, bins=bin_edges)[0]  # Count atoms within each
                                                  # distance interval.

    n[0] = 0

    # \Vref{eq:rdf}:
    rdf = V / N**2 * n / (4 * np.pi * bin_centres**2 * bin_sizes)

    return rdf
#!rdfend!#


if __name__ == "__main__":
    from NAtoms_tasks import boundary_conditions
    import matplotlib.pyplot as plt
    import time

    r, v, t = boundary_conditions()

    nt = r.shape[0]
    r = r.reshape((nt, r.shape[1] // 3, 3))

    num_bins = 100
    rc = 4
    bin_edges = np.linspace(0, rc, num_bins + 1)

    rdf_array = np.zeros(num_bins)
    N = r.shape[0]

    t0 = time.time()
    for i in range(N):
        rdf_array += rdf(bin_edges, r[i], (4 * 1.7)**3)
    t1 = time.time()

    print("RDF time = %.2g s" % (t1-t0))

    plt.plot(0.5 * (bin_edges[1:] + bin_edges[:-1]), rdf_array / N)
    plt.show()
