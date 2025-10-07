from collections import deque
from math import inf

class Solution:
    def maxMoves(self, kx, ky, positions):
        knight_steps = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                        (1, -2), (2, -1), (-1, -2), (-2, -1)]

        pawns_set = set()
        for pos in positions:
            pawns_set.add((pos[0], pos[1]))
        positions = list(pawns_set)
        total_pawns = len(pawns_set)

        from functools import lru_cache

        @lru_cache(None)
        def dp(kx, ky, mask, is_alice):
            if mask == 0:
                return 0

            if is_alice:
                best_moves = 0
            else:
                best_moves = inf

            for idx in range(total_pawns):
                mask_bit = 1 << idx
                if (mask & mask_bit) != 0:
                    pawn_x, pawn_y = positions[idx]

                    nodes_queue = deque()
                    nodes_queue.append((kx, ky, 0))
                    visited_positions = set()
                    visited_positions.add((kx, ky))
                    reached = False
                    steps_count = 0

                    while nodes_queue:
                        cx, cy, steps = nodes_queue.popleft()
                        if (cx, cy) == (pawn_x, pawn_y):
                            reached = True
                            steps_count = steps
                            break
                        for dx, dy in knight_steps:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < 50 and 0 <= ny < 50:
                                if (nx, ny) not in visited_positions:
                                    visited_positions.add((nx, ny))
                                    nodes_queue.append((nx, ny, steps + 1))

                    if reached:
                        updated_mask = mask ^ mask_bit
                        next_player = not is_alice
                        moves_from_here = steps_count + dp(pawn_x, pawn_y, updated_mask, next_player)

                        if is_alice:
                            if best_moves < moves_from_here:
                                best_moves = moves_from_here
                        else:
                            if best_moves > moves_from_here:
                                best_moves = moves_from_here

            return best_moves

        full_mask = (1 << total_pawns) - 1
        return dp(kx, ky, full_mask, True)