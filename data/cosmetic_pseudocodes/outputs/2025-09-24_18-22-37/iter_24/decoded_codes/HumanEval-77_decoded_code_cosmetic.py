from typing import Union


def iscube(number_input: Union[int, float]) -> bool:
    positive_variant: int = int(number_input) if number_input >= 0 else -int(-number_input)
    tentative_root: int = round(abs(positive_variant) ** (1 / 3))
    cubic_computation: int = tentative_root * tentative_root * tentative_root
    return cubic_computation == abs(positive_variant)