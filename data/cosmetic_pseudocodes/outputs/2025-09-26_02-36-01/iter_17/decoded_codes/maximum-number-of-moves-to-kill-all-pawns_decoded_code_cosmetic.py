from collections import deque
from math import inf
from functools import lru_cache

class Solution:
    def maxMoves(self, kx, ky, positions):
        knight_dirs = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        pawns_set = set()
        idx = 0
        while idx < len(positions):
            pawns_set.add((positions[idx][0], positions[idx][1]))
            idx += 1
        positions = list(pawns_set)  # remove duplicates, keep unique pawns only
        total_pawns = len(positions)

        @lru_cache(None)
        def dp(kx, ky, mask, is_alice):
            if mask == 0:
                return 0
            best_value = 0 if is_alice else inf
            for i in range(total_pawns):
                bit_check = 1 << i
                if (mask & bit_check) != 0:
                    target_x, target_y = positions[i]
                    # BFS to find shortest knight path from (kx, ky) to (target_x, target_y)
                    bfs_queue = deque([(kx, ky, 0)])
                    visited_positions = {(kx, ky)}
                    reached = False
                    dist = 0
                    while bfs_queue:
                        curr_x, curr_y, dist = bfs_queue.popleft()
                        if curr_x == target_x and curr_y == target_y:
                            reached = True
                            break
                        for dx, dy in knight_dirs:
                            next_x, next_y = curr_x + dx, curr_y + dy
                            if 0 <= next_x < 50 and 0 <= next_y < 50 and (next_x, next_y) not in visited_positions:
                                visited_positions.add((next_x, next_y))
                                bfs_queue.append((next_x, next_y, dist + 1))
                    if reached:
                        updated_mask = mask ^ bit_check
                        alt_value = dist + dp(target_x, target_y, updated_mask, not is_alice)
                        if is_alice:
                            if best_value < alt_value:
                                best_value = alt_value
                        else:
                            if best_value > alt_value:
                                best_value = alt_value
            return best_value

        initial_mask = (1 << total_pawns) - 1
        return dp(kx, ky, initial_mask, True)