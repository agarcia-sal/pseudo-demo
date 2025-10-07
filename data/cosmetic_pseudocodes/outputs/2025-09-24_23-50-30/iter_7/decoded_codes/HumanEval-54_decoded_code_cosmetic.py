from typing import Dict

def same_chars(param_a: str, param_b: str) -> bool:
    temp_dict_a: Dict[str, bool] = {}
    temp_dict_b: Dict[str, bool] = {}

    for char_x in param_a:
        temp_dict_a[char_x] = True

    for char_y in param_b:
        temp_dict_b[char_y] = True

    set_a = temp_dict_a.keys()
    set_b = temp_dict_b.keys()

    if len(set_a) - len(set_b) != 0:
        return False

    for element_z in set_a:
        if element_z not in set_b:
            return False

    return True