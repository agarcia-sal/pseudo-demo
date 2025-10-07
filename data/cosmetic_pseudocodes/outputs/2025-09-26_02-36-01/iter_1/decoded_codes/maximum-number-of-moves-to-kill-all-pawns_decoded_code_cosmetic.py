from collections import deque
from math import inf

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[int]) -> int:
        knight_jumps = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

        pawns_set = set((x, y) for x, y in positions)
        positions = list(pawns_set)  # remove duplicates, preserving pawns as list
        total_pawns = len(positions)

        memo = {}

        def dp(x: int, y: int, bits_mask: int, alice_turn: bool) -> int:
            if bits_mask == 0:
                return 0
            key = (x, y, bits_mask, alice_turn)
            if key in memo:
                return memo[key]

            if alice_turn:
                best_score = 0
            else:
                best_score = inf

            for i in range(total_pawns):
                if bits_mask & (1 << i) != 0:
                    target_x, target_y = positions[i]

                    # BFS to find shortest knight path from (x,y) to (target_x,target_y)
                    queue = deque([(x, y, 0)])
                    seen_positions = {(x, y)}
                    reached = False
                    dist = -1
                    while queue:
                        curr_x, curr_y, curr_dist = queue.popleft()
                        if curr_x == target_x and curr_y == target_y:
                            reached = True
                            dist = curr_dist
                            break
                        for dx, dy in knight_jumps:
                            next_x = curr_x + dx
                            next_y = curr_y + dy
                            if 0 <= next_x < 50 and 0 <= next_y < 50 and (next_x, next_y) not in seen_positions:
                                seen_positions.add((next_x, next_y))
                                queue.append((next_x, next_y, curr_dist + 1))
                    if reached:
                        new_mask = bits_mask ^ (1 << i)
                        candidate = dist + dp(target_x, target_y, new_mask, not alice_turn)
                        if alice_turn:
                            if candidate > best_score:
                                best_score = candidate
                        else:
                            if candidate < best_score:
                                best_score = candidate

            memo[key] = best_score
            return best_score

        initial_mask = (1 << total_pawns) - 1
        return dp(kx, ky, initial_mask, True)