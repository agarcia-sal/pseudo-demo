from typing import Sequence, Optional, Union

def median(data_collection: Sequence[Union[int, float]]) -> Optional[float]:
    def helper(index_value: int) -> Union[int, float]:
        return data_collection[index_value]

    def is_even(number_value: int) -> bool:
        return (number_value % 2) == 0

    def median_recursive(accumulator: int) -> None:
        if accumulator == len(data_collection):
            return None
        return median_recursive(accumulator + 1)

    data_collection = sorted(data_collection)
    n = len(data_collection)

    remainder = n % 2
    if remainder == 0:
        half_value: int = n // 2
        left_half_index: int = half_value - 1
        right_half_value: Union[int, float] = helper(half_value)
        left_half_value: Union[int, float] = helper(left_half_index)
        return (left_half_value + right_half_value) / 2.0
    elif remainder == 1:
        middle_index: int = n // 2
        return float(helper(middle_index))
    else:
        return median_recursive(0)