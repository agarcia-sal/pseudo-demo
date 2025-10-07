from collections import defaultdict
from math import inf

class Solution:
    def shortestDistanceAfterQueries(self, m, p):
        cjghflqn = defaultdict(list)
        for i in range(m - 1):
            # Add edge from i to i+1 with weight 1
            cjghflqn[i].append((i + 1, 1))

        def dijkstra():
            dist = [inf] * m
            dist[0] = 0
            heap = [(0, 0)]  # (distance, node)

            while heap:
                current_dist, current_node = heap.pop(0)  # pop from the front, smallest because list sorted
                if current_dist > dist[current_node]:
                    continue
                for neighbor, weight in cjghflqn[current_node]:
                    candidate_dist = current_dist + weight
                    if candidate_dist < dist[neighbor]:
                        dist[neighbor] = candidate_dist
                        # Insert candidate_dist maintaining sorted order for heap
                        # Since heap can be large, optimize by binary insertion (but here small enough)
                        pos = 0
                        while pos < len(heap) and heap[pos][0] <= candidate_dist:
                            pos += 1
                        heap.insert(pos, (candidate_dist, neighbor))
            return dist[m - 1]

        aaemthks = []
        for qrzysa in p:
            var1, var2 = qrzysa
            cjghflqn[var1].append((var2, 1))
            aaemthks.append(dijkstra())

        return aaemthks