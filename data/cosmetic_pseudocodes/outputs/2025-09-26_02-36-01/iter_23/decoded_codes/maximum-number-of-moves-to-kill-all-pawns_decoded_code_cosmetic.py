from math import inf
from functools import lru_cache

class Solution:
    def maxMoves(self, kx, ky, positions):
        knight_offsets = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        pawns_set = set()

        def insert_pawns(index):
            if index >= len(positions):
                return
            current_pos = positions[index]
            key = (current_pos[0], current_pos[1])
            pawns_set.add(key)
            insert_pawns(index + 1)

        insert_pawns(0)

        total_pawns = len(pawns_set)
        # remap pawns to original order to preserve positions indexing
        # Positions may have duplicates, pawns_set has unique positions
        # We'll rely on original positions list indexing, so that bit indexes match positions

        @lru_cache(None)
        def dp(rec_kx, rec_ky, bitmask, alice_turn):
            if bitmask == 0:
                return 0
            score = 0 if alice_turn else inf

            def explore_pawn(bitidx):
                if bitidx >= total_pawns:
                    return
                if (bitmask & (1 << bitidx)) != 0:
                    px, py = positions[bitidx]

                    search_queue = [(rec_kx, rec_ky, 0)]
                    visited_nodes = {(rec_kx, rec_ky)}
                    reached = False
                    step_count = 0

                    def bfs_process(queue_index):
                        nonlocal reached, step_count
                        if queue_index >= len(search_queue) or reached:
                            return
                        cx, cy, sc = search_queue[queue_index]
                        if cx == px and cy == py:
                            reached = True
                            step_count = sc
                            return
                        for dx, dy in knight_offsets:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in visited_nodes:
                                visited_nodes.add((nx, ny))
                                search_queue.append((nx, ny, sc + 1))
                        bfs_process(queue_index + 1)

                    bfs_process(0)

                    if reached:
                        updated_mask = bitmask ^ (1 << bitidx)
                        recursive_val = dp(px, py, updated_mask, not alice_turn)
                        total_moves = step_count + recursive_val
                        if alice_turn:
                            if score < total_moves:
                                score = total_moves
                        else:
                            if score > total_moves:
                                score = total_moves
                explore_pawn(bitidx + 1)

            explore_pawn(0)
            return score

        full_mask = (1 << total_pawns) - 1
        return dp(kx, ky, full_mask, True)