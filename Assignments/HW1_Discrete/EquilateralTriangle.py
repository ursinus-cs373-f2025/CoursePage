## Programmer: Chris Tralie
## Purpose: An empirical exploration of the following claim:
# Given 33 points in an equilateral triangle, prove that there are two points
# that are at most a distance of 1/8 = 0.125 from each other

import numpy as np
import matplotlib.pyplot as plt

def get_dists(X):
    """
    Compute all pairwise distances between points in a Euclidean
    point cloud

    Parameters
    ----------
    X: ndarray(N, d)
        Point cloud: points along rows
    """
    XSqr = np.sum(X**2, axis=1)
    D = XSqr[:, None] + XSqr[None, :] - 2*X.dot(X.T)
    D[D < 0] = 0
    return np.sqrt(D)

def get_greedy_perm(X, n_perm=None):
    """
    Compute a furthest point sampling permutation of a set of points
    Parameters
    ----------
    X: ndarray (n_samples, n_features)
        A numpy array of either data or distance matrix
    n_perm: int
        Number of points to take in the permutation
    
    Returns
    -------
    idx_perm: ndarray(n_perm)
        Indices of points in the greedy permutation
    """
    if not n_perm:
        n_perm = X.shape[0]
    # By default, takes the first point in the list to be the
    # first point in the permutation, but could be random
    idx_perm = np.zeros(n_perm, dtype=np.int64)
    dpoint2all = lambda i: np.sqrt(np.sum((X[i, :][None, :] - X)**2, axis=1))
    ds = dpoint2all(0)
    dperm2all = [ds]
    for i in range(1, n_perm):
        idx = np.argmax(ds)
        idx_perm[i] = idx
        dperm2all.append(dpoint2all(idx))
        ds = np.minimum(ds, dperm2all[-1])
    return idx_perm

n_samples = 10000 # Number of initial samples to take
n_points = 17 # Final number of samples to take

a = np.array([[0, 0]])
b = np.array([[1, 0]])
c = np.array([[0.5, np.sqrt(3)/2]])

n_experiments = 100
max_min = 0
for experiment in range(n_experiments):
    ## Step 1: Sample n_samples points uniformly by area in the triangle
    bary = np.random.rand(n_samples, 3)
    bary = bary/np.sum(bary, axis=1, keepdims=True)
    X = bary[:, 0][:, None]*a + bary[:, 1][:, None]*b + bary[:, 2][:, None]*c
    
    ## Step 2: Do furthest point sampling to find n_points points
    ## and compute the pair that achieves the minimum distance
    X = X[get_greedy_perm(X, n_points), :]
    D = get_dists(X)
    np.fill_diagonal(D, np.inf)
    idx = np.argmin(D)
    (i, j) = np.unravel_index(idx, D.shape)
    if D[i, j] > max_min:
        max_min = D[i, j]
        print(max_min)
        
    ## Step 3: Plot the results
    plt.clf()
    plt.plot([a[0][0], b[0][0], c[0][0], a[0][0]], [a[0][1], b[0][1], c[0][1], a[0][1]])
    plt.scatter(X[:, 0], X[:, 1], s=3)
    plt.plot(X[[i, j], 0], X[[i, j], 1])

    plt.title("Dist: {:.4f}, Max So Far: {:.4f}".format(D[i, j], max_min))
    plt.savefig("Experiment{}.png".format(experiment))
