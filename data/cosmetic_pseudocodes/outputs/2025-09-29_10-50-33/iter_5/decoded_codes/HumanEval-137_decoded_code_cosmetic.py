from typing import Optional, Union


def compare_one(original_first: Union[str, float, int], original_second: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    modified_first: Union[str, float, int] = original_first
    modified_second: Union[str, float, int] = original_second

    if isinstance(modified_first, str):
        modified_first = modified_first.replace(',', '.', 1)

    if isinstance(modified_second, str):
        modified_second = modified_second.replace(',', '.', 1)

    number_first = float(modified_first)
    number_second = float(modified_second)

    if number_first == number_second:
        return None

    return original_first if number_first > number_second else original_second