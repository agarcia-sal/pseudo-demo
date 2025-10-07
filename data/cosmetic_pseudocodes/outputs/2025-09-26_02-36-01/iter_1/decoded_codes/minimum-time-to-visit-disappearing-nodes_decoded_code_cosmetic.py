from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            source, target, length = edge
            graph[source].append((target, length))
            graph[target].append((source, length))

        distances = [float('inf')] * n
        distances[0] = 0
        priority_queue = [(0, 0)]  # (cost, node)

        while priority_queue:
            current_cost, node = heapq.heappop(priority_queue)

            if current_cost >= disappear[node]:
                continue

            if current_cost > distances[node]:
                continue

            for adjacent, length in graph[node]:
                new_cost = current_cost + length

                if new_cost < distances[adjacent] and new_cost < disappear[adjacent]:
                    distances[adjacent] = new_cost
                    heapq.heappush(priority_queue, (new_cost, adjacent))

        answer = [-1] * n
        for index in range(n):
            if distances[index] < disappear[index]:
                answer[index] = distances[index]

        return answer