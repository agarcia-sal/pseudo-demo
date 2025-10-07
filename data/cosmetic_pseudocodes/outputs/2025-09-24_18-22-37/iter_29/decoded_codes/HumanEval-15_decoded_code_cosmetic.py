from typing import List


def string_sequence(num_x: int) -> str:
    list_y: List[str] = []
    index_z: int = 0
    while index_z <= num_x:
        temp_s: str = str(index_z)
        list_y.append(temp_s)
        index_z += 1
    return " ".join(list_y)