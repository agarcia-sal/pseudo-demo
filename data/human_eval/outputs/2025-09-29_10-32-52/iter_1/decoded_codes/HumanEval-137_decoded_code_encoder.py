from typing import Optional, Union

def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    temp_a = a
    temp_b = b
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')
    float_a = float(temp_a)
    float_b = float(temp_b)
    if float_a == float_b:
        return None
    if float_a > float_b:
        return a
    else:
        return b