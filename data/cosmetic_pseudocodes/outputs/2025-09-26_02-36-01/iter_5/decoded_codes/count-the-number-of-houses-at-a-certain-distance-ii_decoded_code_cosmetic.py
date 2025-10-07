from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if not (x <= y):
            x, y = y, x

        def bfs(origin: int) -> list[int]:
            visited_flags = [False] * (n + 1)
            dist_values = [0] * (n + 1)
            dq = deque([origin])
            visited_flags[origin] = True

            def processQueue(dq: deque):
                if len(dq) == 0:
                    return
                current_node = dq.popleft()
                adjacents = [current_node - 1, current_node + 1]

                for neighbor_candidate in adjacents:
                    if 1 <= neighbor_candidate <= n and not visited_flags[neighbor_candidate]:
                        visited_flags[neighbor_candidate] = True
                        dist_values[neighbor_candidate] = dist_values[current_node] + 1
                        dq.append(neighbor_candidate)

                if current_node == x and not visited_flags[y]:
                    visited_flags[y] = True
                    dist_values[y] = dist_values[current_node] + 1
                    dq.append(y)
                elif current_node == y and not visited_flags[x]:
                    visited_flags[x] = True
                    dist_values[x] = dist_values[current_node] + 1
                    dq.append(x)

                processQueue(dq)

            processQueue(dq)
            return dist_values[1:]

        frequency_counts = [0] * n

        def iterateIndices(current_index: int):
            if current_index > n:
                return

            distance_results = bfs(current_index)

            def updateFrequencies(lst: list[int], idx: int):
                if idx > len(lst):
                    return
                individual_distance = lst[idx - 1]
                if individual_distance > 0:
                    frequency_counts[individual_distance - 1] += 1
                updateFrequencies(lst, idx + 1)

            updateFrequencies(distance_results, 1)
            iterateIndices(current_index + 1)

        iterateIndices(1)

        return frequency_counts