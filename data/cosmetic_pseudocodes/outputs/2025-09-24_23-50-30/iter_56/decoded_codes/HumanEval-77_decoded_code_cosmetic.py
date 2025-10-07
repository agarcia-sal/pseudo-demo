from typing import Union

def iscube(numeric_input: Union[int, float]) -> bool:
    transformed_input = numeric_input if numeric_input >= 0 else -numeric_input
    approx_root = round(transformed_input ** (1 / 3))
    verification_cube = approx_root * approx_root * approx_root
    return verification_cube == transformed_input