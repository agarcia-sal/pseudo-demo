from typing import List

class Solution:

    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:

        def traverseTree(node: int, parent: int, distances: List[int]) -> None:
            for neighbor in g[node]:
                if neighbor != parent:
                    distances[neighbor] = distances[node] + 1
                    traverseTree(neighbor, node, distances)

        size = len(edges) + 1
        g = [[] for _ in range(size)]

        for u_, v_ in edges:
            g[u_].append(v_)
            g[v_].append(u_)

        distAlpha = [-1] * size
        distAlpha[0] = 0
        traverseTree(0, -1, distAlpha)

        maxIndexAlpha = 0
        valAlpha = distAlpha[0]
        for i in range(1, size):
            if distAlpha[i] > valAlpha:
                maxIndexAlpha = i
                valAlpha = distAlpha[i]

        distBeta = [-1] * size
        distBeta[maxIndexAlpha] = 0
        traverseTree(maxIndexAlpha, -1, distBeta)

        maxIndexBeta = 0
        valBeta = distBeta[0]
        for i in range(1, size):
            if distBeta[i] > valBeta:
                maxIndexBeta = i
                valBeta = distBeta[i]

        distGamma = [-1] * size
        distGamma[maxIndexBeta] = 0
        traverseTree(maxIndexBeta, -1, distGamma)

        finalOutput = []
        for pos in range(size):
            val1 = distBeta[pos]
            val2 = distGamma[pos]
            if val1 - val2 == 1 or val1 - val2 > 0:
                finalOutput.append(maxIndexAlpha)
            else:
                finalOutput.append(maxIndexBeta)

        return finalOutput