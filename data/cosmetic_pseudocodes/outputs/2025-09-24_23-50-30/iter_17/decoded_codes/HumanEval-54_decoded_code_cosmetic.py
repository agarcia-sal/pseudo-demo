from typing import Dict

def same_chars(alpha: str, beta: str) -> bool:
    set_x: Dict[str, bool] = {}
    set_y: Dict[str, bool] = {}

    for char_x in alpha:
        set_x[char_x] = True

    for char_y in beta:
        set_y[char_y] = True

    keys_x = []
    keys_y = []

    for key in set_x:
        keys_x.append(key)

    for key in set_y:
        keys_y.append(key)

    if len(keys_x) != len(keys_y):
        return False

    for index in range(len(keys_x)):
        if keys_x[index] not in set_y:
            return False

    return True