from typing import List


def make_a_pile(magnitude_p: int) -> List[int]:
    collection_r: List[int] = []
    pointer_z: int = 0
    boundary_c: int = magnitude_p - 1
    while pointer_z <= boundary_c:
        computed_w: int = magnitude_p + (pointer_z * 2)
        collection_r.append(computed_w)
        pointer_z += 1
    return collection_r