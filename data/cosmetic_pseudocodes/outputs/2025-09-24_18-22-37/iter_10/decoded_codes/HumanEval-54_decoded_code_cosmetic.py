from typing import Set

def same_chars(parameter_zed: str, parameter_yit: str) -> bool:
    temp_u: Set[str] = set(parameter_zed)
    temp_v: Set[str] = set(parameter_yit)
    return temp_u == temp_v