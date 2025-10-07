from typing import Union


def rounded_avg(x: int, y: int) -> Union[str, int]:
    if not (y >= x):
        return -1

    sum_accumulator: int = 0
    index_pointer: int = x

    while index_pointer <= y:
        sum_accumulator += index_pointer
        index_pointer += 1

    count_elements: int = (y - x) + 1
    averaging_value: float = sum_accumulator / count_elements
    nearest_whole: int = int(averaging_value + 0.5)  # floor-based rounding alternative
    binary_output: str = format(nearest_whole, "b")
    return binary_output