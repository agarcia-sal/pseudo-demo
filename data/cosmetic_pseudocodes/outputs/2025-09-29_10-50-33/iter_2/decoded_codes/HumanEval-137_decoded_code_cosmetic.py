from typing import Optional, Union


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    first_val: Union[str, float, int] = a
    second_val: Union[str, float, int] = b

    if isinstance(first_val, str):
        first_val = first_val.replace(",", ".")
    if isinstance(second_val, str):
        second_val = second_val.replace(",", ".")

    # Convert to float, allowing int inputs as well
    num_1 = float(first_val)
    num_2 = float(second_val)

    if num_1 == num_2:
        return None
    return a if num_1 > num_2 else b