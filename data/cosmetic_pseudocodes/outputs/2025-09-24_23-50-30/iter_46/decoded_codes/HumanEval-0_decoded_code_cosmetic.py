from typing import Sequence


def has_close_elements(collection_x: Sequence[int], limit_y: int) -> bool:
    def check_pairs(position_a: int) -> bool:
        if position_a >= len(collection_x):
            return False

        def inner_loop(position_b: int) -> bool:
            if position_b >= len(collection_x):
                return check_pairs(position_a + 1)
            if position_a == position_b:
                return inner_loop(position_b + 1)
            gap_z = (
                collection_x[position_b] - collection_x[position_a]
                if collection_x[position_a] < collection_x[position_b]
                else collection_x[position_a] - collection_x[position_b]
            )
            if not (limit_y <= gap_z):
                return True
            return inner_loop(position_b + 1)

        return inner_loop(0)

    return check_pairs(0)