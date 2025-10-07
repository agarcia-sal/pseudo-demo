from typing import Union, Optional


def compare_one(x_one: Union[str, float, int], y_one: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    intermediary_x: Union[str, float, int] = x_one
    intermediary_y: Union[str, float, int] = y_one

    if isinstance(intermediary_x, str):
        intermediary_x = intermediary_x.replace(',', '.')

    if isinstance(intermediary_y, str):
        intermediary_y = intermediary_y.replace(',', '.')

    while True:
        num_x = float(intermediary_x)
        num_y = float(intermediary_y)
        if num_x == num_y:
            break
        elif not (num_x <= num_y):
            return x_one
        else:
            return y_one

    return None