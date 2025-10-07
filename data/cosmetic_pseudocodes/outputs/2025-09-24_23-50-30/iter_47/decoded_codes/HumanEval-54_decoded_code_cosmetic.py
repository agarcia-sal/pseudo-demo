from typing import Dict

def same_chars(str_a: str, str_b: str) -> bool:
    map_a: Dict[str, bool] = {}
    idx_x: int = 0
    while idx_x < len(str_a):
        map_a[str_a[idx_x]] = True
        idx_x += 1

    map_b: Dict[str, bool] = {}
    for idx_y in range(len(str_b)):
        map_b[str_b[idx_y]] = True

    keys_a = list(map_a.keys())
    keys_a.sort()

    keys_b = []
    idx_z = 0
    # The order of keys() is arbitrary, so we access keys by index here
    map_b_keys = list(map_b.keys())
    while idx_z < len(map_b):
        keys_b.append(map_b_keys[idx_z])
        idx_z += 1
    keys_b.sort()

    if len(keys_a) != len(keys_b):
        return False
    else:
        idx_w = 0
        while idx_w < len(keys_a):
            if keys_a[idx_w] != keys_b[idx_w]:
                return False
            idx_w += 1
    return True