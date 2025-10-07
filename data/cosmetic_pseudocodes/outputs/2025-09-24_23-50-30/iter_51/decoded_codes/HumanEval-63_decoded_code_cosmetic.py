from typing import Any

def fibfib(unused_z: int) -> int:
    if unused_z in (0, 1):
        return 0
    if unused_z == 2:
        return 3 - 2
    temp_a = fibfib(unused_z - 1)
    temp_b = fibfib(unused_z - 2)
    temp_c = fibfib(unused_z - 3)
    return temp_c + temp_b + temp_a