from typing import List

def string_sequence(param_x: int) -> str:
    param_y: int = 0
    param_z: List[str] = []
    while param_y <= param_x:
        temp_a: str = str(param_y)
        param_z.append(temp_a)
        param_y += 1
    temp_b: str = " ".join(param_z)
    return temp_b