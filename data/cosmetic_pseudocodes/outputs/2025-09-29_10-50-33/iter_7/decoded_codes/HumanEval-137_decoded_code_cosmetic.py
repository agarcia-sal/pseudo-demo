from typing import Optional, Union


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    clone_x = a
    clone_y = b

    if isinstance(clone_x, str):
        clone_x = clone_x.replace(',', '.')

    if isinstance(clone_y, str):
        clone_y = clone_y.replace(',', '.')

    try:
        float_x = float(clone_x)
        float_y = float(clone_y)
    except (ValueError, TypeError):
        # If conversion to float fails, treat them as unequal so function returns accordingly
        if str(clone_x) == str(clone_y):
            return None
        return a if str(clone_x) > str(clone_y) else b

    if float_x == float_y:
        return None

    return a if float_x > float_y else b