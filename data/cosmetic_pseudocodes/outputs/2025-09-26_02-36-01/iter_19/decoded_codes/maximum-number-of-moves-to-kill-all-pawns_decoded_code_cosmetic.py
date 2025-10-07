from collections import deque
from math import inf
from functools import lru_cache

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        KNIGHT_DIRECTIONS = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        pawn_set = {(pos[0], pos[1]) for pos in positions}
        total_pawns = len(pawn_set)
        positions = list(pawn_set)  # Ensure unique positions with consistent indexing

        @lru_cache(None)
        def dp(cx: int, cy: int, bitmask: int, alice_turn: bool) -> int:
            if bitmask == 0:
                return 0

            result_value = 0 if alice_turn else inf

            for iter_index in range(total_pawns):
                bit_check = 1 << iter_index
                if (bitmask & bit_check) != 0:
                    target_x, target_y = positions[iter_index]

                    # BFS to find shortest knight path from (cx, cy) to (target_x, target_y)
                    visit_queue = deque([(cx, cy, 0)])
                    visited_coords = {(cx, cy)}
                    path_found = False
                    step_count = 0

                    while visit_queue:
                        current_x, current_y, step_count = visit_queue.popleft()
                        if current_x == target_x and current_y == target_y:
                            path_found = True
                            break
                        for dx, dy in KNIGHT_DIRECTIONS:
                            next_x, next_y = current_x + dx, current_y + dy
                            if 0 <= next_x < 50 and 0 <= next_y < 50 and (next_x, next_y) not in visited_coords:
                                visited_coords.add((next_x, next_y))
                                visit_queue.append((next_x, next_y, step_count + 1))

                    if path_found:
                        updated_mask = bitmask ^ bit_check
                        recursive_eval = step_count + dp(target_x, target_y, updated_mask, not alice_turn)
                        if alice_turn:
                            if result_value < recursive_eval:
                                result_value = recursive_eval
                        else:
                            if result_value > recursive_eval:
                                result_value = recursive_eval

            return result_value

        full_mask = (1 << total_pawns) - 1
        return dp(kx, ky, full_mask, True)