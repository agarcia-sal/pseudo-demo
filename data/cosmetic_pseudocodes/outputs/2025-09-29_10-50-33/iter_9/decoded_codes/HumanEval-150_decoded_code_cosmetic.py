from typing import Union


def x_or_y(n: int, x: Union[int, str], y: Union[int, str]) -> Union[int, str]:
    def output_x() -> Union[int, str]:
        # Break not applicable in this context; return immediately
        return x

    def output_y() -> Union[int, str]:
        # Break not applicable in this context; return immediately
        return y

    def check_divisor(current: int) -> Union[int, str]:
        if current >= n:
            return output_x()
        if n % current == 0:
            return output_y()
        return check_divisor(current + 1)

    if n == 1:
        return y
    return check_divisor(2)