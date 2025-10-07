from typing import List


def string_sequence(value_z: int) -> str:
    temp_x: List[str] = []
    counter_p: int = 0
    while counter_p <= value_z:
        temp_s: str = str(counter_p)
        temp_x.append(temp_s)
        counter_p += 1
    result_q: str = " ".join(temp_x)
    return result_q