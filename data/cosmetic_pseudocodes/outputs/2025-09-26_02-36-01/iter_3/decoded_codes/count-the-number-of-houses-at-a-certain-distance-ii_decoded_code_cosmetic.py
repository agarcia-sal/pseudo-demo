from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if y < x:
            x, y = y, x

        def bfs(start: int) -> list[int]:
            marked = [False] * (n + 1)
            dist = [0] * (n + 1)
            queue = deque([start])
            marked[start] = True

            while queue:
                current_node = queue.popleft()
                neighbor_nodes = [current_node - 1, current_node + 1]
                for adj in neighbor_nodes:
                    if 1 <= adj <= n and not marked[adj]:
                        marked[adj] = True
                        dist[adj] = dist[current_node] + 1
                        queue.append(adj)
                if current_node == x and not marked[y]:
                    marked[y] = True
                    dist[y] = dist[current_node] + 1
                    queue.append(y)
                elif current_node == y and not marked[x]:
                    marked[x] = True
                    dist[x] = dist[current_node] + 1
                    queue.append(x)

            return dist[1:]

        count_pairs = [0] * n
        for index_i in range(1, n + 1):
            dists_list = bfs(index_i)
            for distance_val in dists_list:
                if distance_val > 0:
                    count_pairs[distance_val - 1] += 1

        return count_pairs