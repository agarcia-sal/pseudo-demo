from typing import Union


def x_or_y(count: int, a: int, b: int) -> Union[int, None]:
    if count - 1 == 0:
        return b
    else:
        index = 2
        while index < count:
            if index * (count // index) == count:
                return b
            index += 1
        # If no divisor found in [2..count-1], return a
        return a