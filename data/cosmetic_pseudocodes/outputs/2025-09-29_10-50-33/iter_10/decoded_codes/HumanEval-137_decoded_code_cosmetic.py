from functools import reduce
from typing import Optional, Union


def compare_one(a: Union[str, float, int], b: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    omega: Union[str, float, int] = a
    sigma: Union[str, float, int] = b

    if isinstance(omega, str):
        # Replace ',' with '.' in omega
        omega = ''.join('.' if ch == ',' else ch for ch in omega)

    if isinstance(sigma, str):
        # Replace ',' with '.' in sigma using reduce
        sigma = reduce(lambda acc, ch: acc + ('.' if ch == ',' else ch), sigma, "")

    convert_a: float = float(omega)  # type: ignore
    convert_b: float = float(sigma)  # type: ignore

    if not (convert_a != convert_b):
        return None

    return a if convert_a > convert_b else b