from functools import lru_cache
from collections import deque

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: list[list[int]]) -> int:
        knight_shift_pairs = [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]
        occupied_positions = set()

        def convertPositionsToSet(pos_list, occupied_set):
            idx = 0
            while idx < len(pos_list):
                current_item = pos_list[idx]
                occupied_set.add((current_item[0], current_item[1]))
                idx += 1

        convertPositionsToSet(positions, occupied_positions)
        count_pawns = len(occupied_positions)

        # We'll work directly on original positions list for indexing
        # positions contains the target pawns positions

        @lru_cache(None)
        def dp(cur_x: int, cur_y: int, bitmask: int, alice_turn: bool) -> int:
            if bitmask == 0:
                return 0

            candidate_value = 0 if alice_turn else float('inf')

            def bfs_search(start_x: int, start_y: int, target_x: int, target_y: int) -> int:
                visited_coord_set = set()
                queue_list = deque([(start_x, start_y, 0)])
                visited_coord_set.add((start_x, start_y))

                while queue_list:
                    pos_x, pos_y, dist = queue_list.popleft()
                    if pos_x == target_x and pos_y == target_y:
                        return dist

                    for move_dx, move_dy in knight_shift_pairs:
                        new_x = pos_x + move_dx
                        new_y = pos_y + move_dy

                        if 0 <= new_x < 50 and 0 <= new_y < 50 and (new_x, new_y) not in visited_coord_set:
                            visited_coord_set.add((new_x, new_y))
                            queue_list.append((new_x, new_y, dist + 1))

                return -1

            idx_p = 0
            while idx_p < count_pawns:
                bit_flag = 1 << idx_p
                if (bitmask & bit_flag) != 0:
                    current_position = positions[idx_p]
                    target_x, target_y = current_position[0], current_position[1]

                    steps_found = bfs_search(cur_x, cur_y, target_x, target_y)
                    if steps_found != -1:
                        updated_mask = bitmask ^ bit_flag
                        recursive_call_value = dp(target_x, target_y, updated_mask, not alice_turn)
                        total_steps = steps_found + recursive_call_value

                        if alice_turn:
                            if candidate_value < total_steps:
                                candidate_value = total_steps
                        else:
                            if candidate_value > total_steps:
                                candidate_value = total_steps
                idx_p += 1

            return candidate_value

        full_mask_value = (1 << count_pawns) - 1
        return dp(kx, ky, full_mask_value, True)