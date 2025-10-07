import heapq
from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        adjacency = defaultdict(list)
        for x, y, w in edges:
            adjacency[x].append((y, w))
            adjacency[y].append((x, w))

        dist = [inf] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            d, node = heapq.heappop(heap)

            if d >= disappear[node]:
                continue

            if d > dist[node]:
                continue

            for adjNode, lengthValue in adjacency[node]:
                newDist = d + lengthValue
                if newDist < dist[adjNode] and newDist < disappear[adjNode]:
                    dist[adjNode] = newDist
                    heapq.heappush(heap, (newDist, adjNode))

        output = [-1] * n
        for index in range(n):
            if dist[index] < disappear[index]:
                output[index] = dist[index]

        return output