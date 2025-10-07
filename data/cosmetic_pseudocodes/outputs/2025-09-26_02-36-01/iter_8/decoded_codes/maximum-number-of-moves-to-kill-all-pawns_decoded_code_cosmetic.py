from collections import deque
from math import inf

class Solution:
    def maxMoves(self, kx, ky, positions):
        KNIGHT_STEPS = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        pawn_set = set()
        idx_pos = 0
        while idx_pos < len(positions):
            pawn_set.add((positions[idx_pos][0], positions[idx_pos][1]))
            idx_pos += 1
        positions = list(pawn_set)
        pawn_count = len(pawn_set)
        memo = {}

        def dp(kx, ky, mask, is_alice):
            if mask == 0:
                return 0
            key = (kx, ky, mask, is_alice)
            if key in memo:
                return memo[key]
            if is_alice:
                move_agg = -inf
            else:
                move_agg = inf

            for index_iter in range(pawn_count):
                if (mask & (1 << index_iter)) != 0:
                    curr_px, curr_py = positions[index_iter]
                    # BFS to find minimum knight moves from (kx, ky) to (curr_px, curr_py)
                    bfs_queue = deque([(kx, ky, 0)])
                    seen_set = {(kx, ky)}
                    found_flag = False
                    while bfs_queue:
                        current_x, current_y, current_steps = bfs_queue.popleft()
                        if current_x == curr_px and current_y == curr_py:
                            found_flag = True
                            break
                        for dx, dy in KNIGHT_STEPS:
                            next_x, next_y = current_x + dx, current_y + dy
                            if 0 <= next_x < 50 and 0 <= next_y < 50:
                                if (next_x, next_y) not in seen_set:
                                    seen_set.add((next_x, next_y))
                                    bfs_queue.append((next_x, next_y, current_steps + 1))
                    if found_flag:
                        next_mask = mask ^ (1 << index_iter)
                        cand_sum = current_steps + dp(curr_px, curr_py, next_mask, not is_alice)
                        if is_alice:
                            if cand_sum > move_agg:
                                move_agg = cand_sum
                        else:
                            if cand_sum < move_agg:
                                move_agg = cand_sum
            memo[key] = move_agg
            return move_agg

        full_mask = (1 << pawn_count) - 1
        return dp(kx, ky, full_mask, True)