from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if not (x <= y):
            x, y = y, x

        def bfs(start: int) -> list[int]:
            visit_status = [0] * (n + 1)
            dist_arr = [0] * (n + 1)
            fifo_queue = deque([start])
            visit_status[start] = 1

            while fifo_queue:
                current_pos = fifo_queue.popleft()
                for neighbor_pos in (current_pos - 1, current_pos + 1):
                    if 1 <= neighbor_pos <= n and visit_status[neighbor_pos] == 0:
                        visit_status[neighbor_pos] = 1
                        dist_arr[neighbor_pos] = dist_arr[current_pos] + 1
                        fifo_queue.append(neighbor_pos)

                if current_pos == x and visit_status[y] == 0:
                    visit_status[y] = 1
                    dist_arr[y] = dist_arr[current_pos] + 1
                    fifo_queue.append(y)
                elif current_pos == y and visit_status[x] == 0:
                    visit_status[x] = 1
                    dist_arr[x] = dist_arr[current_pos] + 1
                    fifo_queue.append(x)

            return dist_arr[1:]

        freq_counter = [0] * n
        for index_i in range(1, n + 1):
            dist_list = bfs(index_i)
            for dist_val in dist_list:
                if dist_val > 0:
                    freq_counter[dist_val - 1] += 1

        return freq_counter