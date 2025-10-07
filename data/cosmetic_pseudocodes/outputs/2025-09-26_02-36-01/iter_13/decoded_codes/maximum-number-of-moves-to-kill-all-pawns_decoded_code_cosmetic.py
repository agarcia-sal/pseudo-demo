from math import inf
from collections import deque

class Solution:
    def maxMoves(self, kx, ky, positions):
        BOARD_LIMIT = 50
        knight_offsets = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

        def buildPawnSet(posList):
            def helper(index, acc):
                if index == len(posList):
                    return acc
                current = (posList[index][0], posList[index][1])
                acc_new = acc | {current}
                return helper(index + 1, acc_new)
            return helper(0, set())

        pawns = buildPawnSet(positions)
        total_pawns = len(pawns)

        # Map positions to indices so that positions[i] is unambiguous with duplicates
        # We must keep the original positions list for order consistency as dp uses positions[i].
        # The problem does not clarify duplicates; we rely on the given positions list as-is.

        from functools import lru_cache

        @lru_cache(None)
        def dp(current_x, current_y, current_mask, alice_turn):
            if current_mask == 0:
                return 0

            best_score = 0 if alice_turn else inf

            def processIndex(i, acc):
                if i == total_pawns:
                    return acc
                current_bit = 1 << i
                if (current_mask & current_bit) != 0:
                    pos_x, pos_y = positions[i]

                    def bfs(queue, visited):
                        if not queue:
                            return False, 0
                        cx, cy, distance = queue[0]
                        rest_queue = queue[1:]

                        if cx == pos_x and cy == pos_y:
                            return True, distance

                        def neighbors(offsets, q, vis):
                            if not offsets:
                                return q, vis
                            dx, dy = offsets[0]
                            nxt_x, nxt_y = cx + dx, cy + dy
                            q_new, vis_new = q, vis
                            cond = 0 <= nxt_x < BOARD_LIMIT and 0 <= nxt_y < BOARD_LIMIT
                            if cond and (nxt_x, nxt_y) not in vis:
                                q_new = q_new + [(nxt_x, nxt_y, distance + 1)]
                                vis_new = vis_new | {(nxt_x, nxt_y)}
                            return neighbors(offsets[1:], q_new, vis_new)

                        queue_updated, visited_updated = neighbors(knight_offsets, rest_queue, visited)
                        return bfs(queue_updated, visited_updated)

                    found_flag, step_count = bfs([(current_x, current_y, 0)], {(current_x, current_y)})

                    if found_flag:
                        new_mask = current_mask ^ current_bit
                        next_turn = not alice_turn
                        next_score = step_count + dp(pos_x, pos_y, new_mask, next_turn)
                        if alice_turn:
                            if next_score > acc:
                                acc = next_score
                        else:
                            if next_score < acc:
                                acc = next_score
                return processIndex(i + 1, acc)

            return processIndex(0, best_score)

        full_mask = (1 << total_pawns) - 1
        return dp(kx, ky, full_mask, True)