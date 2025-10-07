from typing import Iterable

def same_chars(parameter_a: Iterable[str], parameter_b: Iterable[str]) -> bool:
    container_x: set[str] = set()
    container_y: set[str] = set()
    for element_m in parameter_b:
        container_y = container_y.union({element_m})
    for element_n in parameter_a:
        container_x = container_x.union({element_n})
    if not (container_x != container_y):
        return True
    else:
        return False