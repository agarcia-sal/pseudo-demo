from collections import deque

class Solution:
    def maxMoves(self, x_start: int, y_start: int, locs: list) -> int:
        shifts = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        pawn_set = set((pos[0], pos[1]) for pos in locs)
        locs = list(pawn_set)
        total_pawns = len(locs)

        from math import inf

        memo = {}

        def search(cur_x: int, cur_y: int, state_mask: int, alice_turn: bool) -> int:
            if state_mask == 0:
                return 0
            key = (cur_x, cur_y, state_mask, alice_turn)
            if key in memo:
                return memo[key]

            result_value = 0 if alice_turn else inf

            for idx in range(total_pawns):
                if (state_mask & (1 << idx)) != 0:
                    tgt_x, tgt_y = locs[idx]

                    bfs_queue = deque()
                    bfs_queue.append((cur_x, cur_y, 0))
                    visited_coords = {(cur_x, cur_y)}

                    found_flag = False
                    while bfs_queue:
                        curr_x, curr_y, dist = bfs_queue.popleft()
                        if curr_x == tgt_x and curr_y == tgt_y:
                            found_flag = True
                            break
                        for dx, dy in shifts:
                            nxt_x, nxt_y = curr_x + dx, curr_y + dy
                            if 0 <= nxt_x < 50 and 0 <= nxt_y < 50:
                                if (nxt_x, nxt_y) not in visited_coords:
                                    visited_coords.add((nxt_x, nxt_y))
                                    bfs_queue.append((nxt_x, nxt_y, dist + 1))

                    if found_flag:
                        updated_mask = state_mask ^ (1 << idx)
                        next_val = dist + search(tgt_x, tgt_y, updated_mask, not alice_turn)

                        if alice_turn:
                            if next_val > result_value:
                                result_value = next_val
                        else:
                            if next_val < result_value:
                                result_value = next_val

            memo[key] = result_value
            return result_value

        full_mask = (1 << total_pawns) - 1
        return search(x_start, y_start, full_mask, True)