from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        def kruskal_mst(points):
            n = len(points)
            edges = []

            for i in range(n):
                for j in range(i + 1, n):
                    edges.append((i, j, manhattan_distance(points[i], points[j])))

            edges.sort(key=lambda x: x[2])

            parent = [i for i in range(n)]
            rank = [0] * n
            min_spanning_tree = []

            for edge in edges:
                x, y, weight = edge
                x_root = find(parent, x)
                y_root = find(parent, y)

                if x_root != y_root:
                    min_spanning_tree.append(edge)
                    union(parent, rank, x_root, y_root)

            return min_spanning_tree

        min_spanning_tree = kruskal_mst(points)

        min_length = sum(weight for _, _, weight in min_spanning_tree)

        return min_length
