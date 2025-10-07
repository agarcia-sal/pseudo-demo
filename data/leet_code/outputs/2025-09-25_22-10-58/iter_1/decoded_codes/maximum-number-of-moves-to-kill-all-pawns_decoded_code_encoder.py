from collections import deque
from math import inf

class Solution:
    def maxMoves(self, kx, ky, positions):
        # All eight knight moves (dx, dy)
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        pawn_positions = set(tuple(pos) for pos in positions)
        positions = list(pawn_positions)
        num_pawns = len(positions)

        from functools import lru_cache

        @lru_cache(None)
        def dp(kx, ky, mask, is_alice):
            if mask == 0:
                return 0

            if is_alice:
                max_min_moves = 0
            else:
                max_min_moves = inf

            for index in range(num_pawns):
                if (mask & (1 << index)) != 0:
                    px, py = positions[index]
                    queue = deque()
                    queue.append((kx, ky, 0))
                    visited = set()
                    visited.add((kx, ky))
                    found = False

                    while queue:
                        cx, cy, steps = queue.popleft()
                        if cx == px and cy == py:
                            found = True
                            break
                        for dx, dy in knight_moves:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                queue.append((nx, ny, steps + 1))

                    if found:
                        new_mask = mask ^ (1 << index)
                        next_moves = steps + dp(px, py, new_mask, not is_alice)
                        if is_alice:
                            if next_moves > max_min_moves:
                                max_min_moves = next_moves
                        else:
                            if next_moves < max_min_moves:
                                max_min_moves = next_moves

            return max_min_moves

        all_pawns_mask = (1 << num_pawns) - 1
        return dp(kx, ky, all_pawns_mask, True)