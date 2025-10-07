from typing import Tuple

def reverse_delete(str_x: str, str_y: str) -> Tuple[str, bool]:
    res_list = [char for char in str_x if char not in str_y]
    final_str = "".join(res_list)
    return final_str, final_str == final_str[::-1]