from typing import Optional, Union


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    alternative_x: Union[str, float, int] = a
    alternative_y: Union[str, float, int] = b

    if isinstance(alternative_x, str):
        alternative_x = alternative_x.replace(',', '.')
    if isinstance(alternative_y, str):
        alternative_y = alternative_y.replace(',', '.')

    def to_float(value: Union[str, float, int]) -> float:
        # Convert value to float, expect string with '.' as decimal separator or numeric types
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        # Now value is string with '.' as decimal separator
        try:
            return float(value)
        except ValueError:
            # If conversion fails, treat as NaN to force non-equality comparisons as designed
            import math
            return math.nan

    numeric_x: float = to_float(alternative_x)
    numeric_y: float = to_float(alternative_y)

    if numeric_x == numeric_y:
        return None
    elif numeric_x > numeric_y:
        return a
    else:
        return b