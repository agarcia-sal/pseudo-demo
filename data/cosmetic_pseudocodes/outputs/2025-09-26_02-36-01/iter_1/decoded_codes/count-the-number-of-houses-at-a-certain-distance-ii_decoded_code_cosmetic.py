from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if y < x:
            x, y = y, x

        def bfs(source: int) -> list[int]:
            visited_flags = [False] * (n + 1)
            dist_array = [0] * (n + 1)
            processing_queue = deque([source])
            visited_flags[source] = True

            while processing_queue:
                node = processing_queue.popleft()
                neighbors = [node - 1, node + 1]

                for adj in neighbors:
                    if 1 <= adj <= n and not visited_flags[adj]:
                        visited_flags[adj] = True
                        dist_array[adj] = dist_array[node] + 1
                        processing_queue.append(adj)

                if node == x and not visited_flags[y]:
                    visited_flags[y] = True
                    dist_array[y] = dist_array[node] + 1
                    processing_queue.append(y)
                elif node == y and not visited_flags[x]:
                    visited_flags[x] = True
                    dist_array[x] = dist_array[node] + 1
                    processing_queue.append(x)

            return dist_array[1:]

        final_counts = [0] * n

        for position in range(1, n + 1):
            dist_list = bfs(position)
            for val in dist_list:
                if val > 0:
                    final_counts[val - 1] += 1

        return final_counts