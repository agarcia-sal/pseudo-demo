from typing import Union, Optional


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[None]:
    num_x: Union[str, float, int] = a
    num_y: Union[str, float, int] = b

    # Normalize num_x if it's a string by replacing ',' with '.'
    while True:
        if not isinstance(num_x, str):
            break
        replaced_x = []
        index_x = 0
        while True:
            if index_x >= len(num_x):
                break
            ch_x = num_x[index_x]
            replaced_x.append('.' if ch_x == ',' else ch_x)
            index_x += 1
        num_x = ''.join(replaced_x)

    # Normalize num_y if it's a string by replacing ',' with '.'
    while True:
        if not isinstance(num_y, str):
            break
        replaced_y = []
        index_y = 0
        while True:
            if index_y >= len(num_y):
                break
            ch_y = num_y[index_y]
            replaced_y.append('.' if ch_y == ',' else ch_y)
            index_y += 1
        num_y = ''.join(replaced_y)

    val_x = float(num_x)  # float_from_string
    val_y = float(num_y)

    if val_x == val_y:
        pass
    elif val_x > val_y:
        return a
    else:
        return b

    return None