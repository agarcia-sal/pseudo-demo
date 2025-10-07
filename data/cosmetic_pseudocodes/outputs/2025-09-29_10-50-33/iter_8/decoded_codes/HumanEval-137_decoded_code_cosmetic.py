from typing import Union, Optional


def compare_one(x_value: Union[str, float, int], y_value: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    def cleanse_string(input_str: str) -> str:
        return input_str.replace(',', '.')

    alpha: Union[str, float, int] = x_value
    beta: Union[str, float, int] = y_value

    if isinstance(alpha, str):
        alpha = cleanse_string(alpha)

    if isinstance(beta, str):
        beta = cleanse_string(beta)

    def float_eq(val1: Union[str, float, int], val2: Union[str, float, int]) -> bool:
        return float(val1) == float(val2)

    if float_eq(alpha, beta):
        return None

    return x_value if float(alpha) > float(beta) else y_value