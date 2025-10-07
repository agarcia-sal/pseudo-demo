from collections import deque

class Solution:
    def maxMoves(self, kx, ky, positions):
        knight_directions = [(1, 2), (2, 1), (2, -1), (1, -2),
                             (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        pawn_set = set((x, y) for x, y in positions)
        pawn_positions = list(pawn_set)
        pawn_count = len(pawn_positions)

        from math import inf
        memo = {}

        def dp(kx, ky, mask, is_alice):
            if mask == 0:
                return 0

            key = (kx, ky, mask, is_alice)
            if key in memo:
                return memo[key]

            result = 0 if is_alice else inf

            for i in range(pawn_count):
                if (mask & (1 << i)) != 0:
                    target_x, target_y = pawn_positions[i]

                    states = deque()
                    states.append((kx, ky, 0))
                    explored = set()
                    explored.add((kx, ky))

                    found_target = False
                    step_count = 0

                    while states:
                        cx, cy, step = states.popleft()
                        if cx == target_x and cy == target_y:
                            found_target = True
                            step_count = step
                            break

                        for dx, dy in knight_directions:
                            next_x, next_y = cx + dx, cy + dy
                            if 0 <= next_x < 50 and 0 <= next_y < 50 and (next_x, next_y) not in explored:
                                explored.add((next_x, next_y))
                                states.append((next_x, next_y, step + 1))

                    if found_target:
                        updated_mask = mask ^ (1 << i)
                        value = step_count + dp(target_x, target_y, updated_mask, not is_alice)

                        if is_alice:
                            if value > result:
                                result = value
                        else:
                            if value < result:
                                result = value

            memo[key] = result
            return result

        full_mask = (1 << pawn_count) - 1
        return dp(kx, ky, full_mask, True)