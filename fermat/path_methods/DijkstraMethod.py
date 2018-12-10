import heapq

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

from fermat.path_methods.DistanceCalculatorMethod import DistanceCalculatorMethod


class DijkstraMethod(DistanceCalculatorMethod):

    def fit(self, distances):

        adj_matrix = self.create_adj_matrix(distances)
        self.distances = shortest_path(
            csgraph=adj_matrix.power(self.fermat.alpha),
            method='D'
        )

    def create_adj_matrix(self, distances):
        
        k = self.fermat.k 
        n = distances.shape[0]
        
        rows = []
        columns = []
        values = []

        edges = set()

        for i in range(n):
            smallest_values_and_columns = heapq.nsmallest(k, zip(distances[i].tolist()[0], list(range(n))))
            # vs, cs = zip(*smallest_values_and_columns)

            for v, c in smallest_values_and_columns:
                if (i, c) not in edges and (c, i) not in edges:
                    rows.append(i)
                    columns.append(c)
                    values.append(v)
                    edges.add((i, c))

        return csr_matrix((values+values, (rows+columns, columns+rows)), shape=(n, n))

    def get_distance(self, a, b):
        return self.distances[a, b]

    def get_distances(self):
        return self.distances