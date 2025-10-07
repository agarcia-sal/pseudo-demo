from math import inf
from collections import deque
from functools import lru_cache

class Solution:
    def maxMoves(self, kx, ky, positions):
        knight_moves = [
            (2, 1), (1, 2), (2, -1), (-1, 2),
            (-2, 1), (-1, -2), (-2, 1), (1, -2)
        ]

        # Convert positions list into a set of tuples for fast lookup
        pawn_positions = set()
        def to_set(poses, accum):
            for pos in poses:
                accum.add((pos[0], pos[1]))
        to_set(positions, pawn_positions)

        num_pawns = len(pawn_positions)

        # To preserve the index matching with positions list, we need positions as a list of tuples
        positions = [(x, y) for x, y in positions]

        def bit_check(m, idx):
            return (m & (1 << idx)) != 0

        def toggle_bit(m, idx):
            return m ^ (1 << idx)

        def coords_match(x1, y1, x2, y2):
            return x1 == x2 and y1 == y2

        def bfs(start_x, start_y, target_x, target_y):
            queue = deque()
            visited = set()
            queue.append((start_x, start_y, 0))
            visited.add((start_x, start_y))

            while queue:
                cx, cy, steps = queue.popleft()
                if coords_match(cx, cy, target_x, target_y):
                    return steps
                for dx, dy in knight_moves:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny, steps + 1))
            return -1

        @lru_cache(None)
        def dp(kx, ky, mask, is_alice):
            if mask == 0:
                return 0
            max_min_moves = 0 if is_alice else inf

            for idx in range(num_pawns):
                if bit_check(mask, idx):
                    px, py = positions[idx]
                    dist = bfs(kx, ky, px, py)
                    if dist != -1:
                        new_mask = toggle_bit(mask, idx)
                        next_val = dp(px, py, new_mask, not is_alice)
                        total = dist + next_val
                        if is_alice:
                            if total > max_min_moves:
                                max_min_moves = total
                        else:
                            if total < max_min_moves:
                                max_min_moves = total
            return max_min_moves

        all_pawns_mask = (1 << num_pawns) - 1
        return dp(kx, ky, all_pawns_mask, True)