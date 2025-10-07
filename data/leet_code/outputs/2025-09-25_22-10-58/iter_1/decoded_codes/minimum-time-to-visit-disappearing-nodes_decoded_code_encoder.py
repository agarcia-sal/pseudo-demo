import heapq
import math
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def minimumTime(self, n: int, edges: List[Tuple[int, int, int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        distances = [math.inf] * n
        distances[0] = 0

        min_heap = [(0, 0)]  # (distance, node)

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_distance >= disappear[current_node]:
                continue

            if current_distance > distances[current_node]:
                continue

            for neighbor, length in graph[current_node]:
                distance = current_distance + length
                if distance < distances[neighbor] and distance < disappear[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        result = [-1] * n
        for i in range(n):
            if distances[i] < disappear[i]:
                result[i] = distances[i]

        return result