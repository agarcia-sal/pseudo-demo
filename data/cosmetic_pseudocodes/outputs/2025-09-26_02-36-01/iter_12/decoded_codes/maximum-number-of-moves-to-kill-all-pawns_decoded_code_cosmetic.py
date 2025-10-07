from math import inf
from functools import lru_cache
from collections import deque

class Solution:
    def maxMoves(self, kx, ky, positions):
        allowable_moves = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

        stored_positions = {(x, y): True for x, y in positions}
        pawn_count = len(stored_positions)

        def bfsPath(sx, sy, tx, ty):
            q = deque()
            q.append((sx, sy, 0))
            visited_nodes = {(sx, sy)}

            while q:
                cx, cy, dist = q.popleft()

                if cx == tx and cy == ty:
                    return dist

                for mdx, mdy in allowable_moves:
                    nx, ny = cx+mdx, cy+mdy
                    if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visited_nodes:
                        visited_nodes.add((nx, ny))
                        q.append((nx, ny, dist + 1))
            return -1

        full_mask = (1 << pawn_count) - 1

        @lru_cache(None)
        def dp(cx, cy, bitmask, alice_turn):
            if bitmask == 0:
                return 0

            if alice_turn:
                result = 0
            else:
                result = inf

            current = 1
            idx = 0
            positions_list = list(positions)
            while current <= bitmask:
                if bitmask & current:
                    px, py = positions_list[idx]
                    path_len = bfsPath(cx, cy, px, py)
                    if path_len != -1:
                        next_mask = bitmask ^ current
                        candidate = path_len + dp(px, py, next_mask, not alice_turn)
                        if alice_turn:
                            if candidate > result:
                                result = candidate
                        else:
                            if candidate < result:
                                result = candidate
                current <<= 1
                idx += 1

            return result

        return dp(kx, ky, full_mask, True)