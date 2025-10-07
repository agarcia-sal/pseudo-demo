from typing import Sequence


def will_it_fly(collection_x: Sequence[int], limit_z: int) -> bool:
    if limit_z < sum(collection_x):
        return False

    def verify_symmetric(left_pos: int, right_pos: int) -> bool:
        if left_pos >= right_pos:
            return True
        if collection_x[left_pos] != collection_x[right_pos]:
            return False
        return verify_symmetric(left_pos + 1, right_pos - 1)

    return verify_symmetric(0, len(collection_x) - 1)