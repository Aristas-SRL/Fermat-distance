import numpy as np
from scipy.spatial import distance_matrix
from fermat import Fermat

if __name__ == '__main__':

    points = np.array([[0, 0], [1, 0], [1, 1], [2, 1]])
    md = distance_matrix(points, points)

    ff = Fermat(
        alpha=1,
        path_method='D',
        k=1
    )

    ff.fit(np.matrix(md))

    print("aaaaa")
