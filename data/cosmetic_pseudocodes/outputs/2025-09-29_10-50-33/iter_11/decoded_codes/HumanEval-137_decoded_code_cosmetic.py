from typing import Union


def compare_one(alpha: Union[str, float, int], beta: Union[str, float, int]) -> Union[str, None]:
    # Local function to replace commas with dots in strings
    def normalize(value: Union[str, float, int]) -> Union[str, float, int]:
        if isinstance(value, str):
            return ''.join('.' if ch == ',' else ch for ch in value)
        return value

    delta = normalize(alpha)
    epsilon = normalize(beta)

    iota = float(delta)  # Will raise ValueError if not convertible, consistent with pseudocode
    kappa = float(epsilon)

    if iota == kappa:
        return None  # abort null_value

    if iota > kappa:
        return alpha  # abort alpha

    return beta  # abort beta