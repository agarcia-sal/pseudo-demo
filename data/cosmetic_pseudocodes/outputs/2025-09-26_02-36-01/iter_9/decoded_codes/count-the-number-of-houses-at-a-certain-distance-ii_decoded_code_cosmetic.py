from collections import deque

class Solution:
    def countOfPairs(self, p: int, q: int, r: int) -> list[int]:
        if q > r:
            q, r = r, q

        def bfs(seed: int) -> list[int]:
            mark = [False] * (p + 1)
            dist = [0] * (p + 1)
            fifo = deque([seed])
            mark[seed] = True

            while fifo:
                current_node = fifo.popleft()
                adjacent_nodes = [current_node - 1, current_node + 1]

                for neighbor in adjacent_nodes:
                    if 1 <= neighbor <= p and not mark[neighbor]:
                        mark[neighbor] = True
                        dist[neighbor] = dist[current_node] + 1
                        fifo.append(neighbor)

                if current_node == q and not mark[r]:
                    mark[r] = True
                    dist[r] = dist[current_node] + 1
                    fifo.append(r)
                elif current_node == r and not mark[q]:
                    mark[q] = True
                    dist[q] = dist[current_node] + 1
                    fifo.append(q)

            return dist[1:]

        tally = [0] * p

        for loop_index in range(1, p + 1):
            sampled_dist = bfs(loop_index)
            for measure in sampled_dist:
                if measure > 0:
                    tally[measure - 1] += 1

        return tally