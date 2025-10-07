from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(node: int, parent: int, distance: List[int]) -> None:
            stack = [(node, parent)]
            while stack:
                current, prev = stack.pop()
                neighbors = g[current]
                idx = 0
                while idx < len(neighbors):
                    neighbor = neighbors[idx]
                    if neighbor != prev:
                        distance[neighbor] = distance[current] + 1
                        stack.append((neighbor, current))
                    idx += 1

        size = len(edges) + 1
        g = [[] for _ in range(size)]
        for first, second in edges:
            g[first].append(second)
            g[second].append(first)

        distStart = [-1] * size
        distStart[0] = 0
        dfs(0, -1, distStart)

        positionA = 0
        maxDistance = distStart[0]
        for index in range(1, size):
            if distStart[index] > maxDistance:
                maxDistance = distStart[index]
                positionA = index

        distA = [-1] * size
        distA[positionA] = 0
        dfs(positionA, -1, distA)

        positionB = 0
        maxDistB = distA[0]
        for idxB in range(1, size):
            if distA[idxB] > maxDistB:
                maxDistB = distA[idxB]
                positionB = idxB

        distB = [-1] * size
        distB[positionB] = 0
        dfs(positionB, -1, distB)

        outputList = []
        for pos in range(size):
            if distA[pos] > distB[pos]:
                outputList.append(positionA)
            else:
                outputList.append(positionB)

        return outputList