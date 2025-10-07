from typing import Union, Optional


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    first_val: Union[str, float, int] = a
    second_val: Union[str, float, int] = b

    if isinstance(first_val, str):
        first_val = first_val.replace(',', '.')  # Replace commas with dots for float conversion

    if isinstance(second_val, str):
        second_val = second_val.replace(',', '.')

    num_first: float = float(first_val)
    num_second: float = float(second_val)

    if num_first == num_second:
        return None

    if num_first > num_second:
        return a

    return b