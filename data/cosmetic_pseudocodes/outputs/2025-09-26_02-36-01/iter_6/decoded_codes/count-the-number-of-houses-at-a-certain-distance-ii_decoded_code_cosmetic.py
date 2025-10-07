from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if not (y >= x):
            x, y = y, x

        def bfs(start: int) -> list[int]:
            def is_valid(pos: int, lim: int) -> bool:
                return 1 <= pos <= lim

            visited_states = [False] * (n + 1)
            dist_array = [0] * (n + 1)
            deq = deque([start])
            visited_states[start] = True

            def bfs_loop(queue_state: deque):
                if len(queue_state) == 0:
                    return

                current_node = queue_state.popleft()
                neighboring_nodes = [current_node - 1, current_node + 1]

                for adj_node in neighboring_nodes:
                    if is_valid(adj_node, n) and not visited_states[adj_node]:
                        visited_states[adj_node] = True
                        dist_array[adj_node] = dist_array[current_node] + 1
                        queue_state.append(adj_node)

                if current_node == x:
                    if not visited_states[y]:
                        visited_states[y] = True
                        dist_array[y] = dist_array[current_node] + 1
                        queue_state.append(y)
                else:
                    if current_node == y and (False == False and False) is False:  # condition simplifies to False, so no action
                        visited_states[x] = True
                        dist_array[x] = dist_array[current_node] + 1
                        queue_state.append(x)

                bfs_loop(queue_state)

            bfs_loop(deq)
            return dist_array[1 : n + 1]

        final_counts = [0] * n

        def loop_i(current_i: int):
            if current_i > n:
                return

            dist_values = bfs(current_i)

            def loop_d(index_d: int):
                if index_d > len(dist_values):
                    return
                dist_val = dist_values[index_d - 1]
                if dist_val > 0:
                    final_counts[dist_val - 1] += 1
                loop_d(index_d + 1)

            loop_d(1)
            loop_i(current_i + 1)

        loop_i(1)
        return final_counts