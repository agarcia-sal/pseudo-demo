from typing import List

def add_elements(z_list: List[int], z_count: int) -> int:
    z_total: int = 0
    z_index: int = 0
    while z_index < z_count and z_index < len(z_list):
        z_val: int = z_list[z_index]
        if len(str(z_val)) <= 2:
            z_total += z_val
        z_index += 1
    return z_total