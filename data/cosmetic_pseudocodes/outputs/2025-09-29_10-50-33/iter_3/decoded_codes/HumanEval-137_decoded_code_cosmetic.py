from typing import Optional, Union


def compare_one(alpha: Union[str, float, int], beta: Union[str, float, int]) -> Optional[Union[str, float, int]]:
    tempAlpha: Union[str, float, int] = alpha
    tempBeta: Union[str, float, int] = beta

    # Replace commas with dots if the values are strings
    if isinstance(tempAlpha, str):
        tempAlpha = tempAlpha.replace(',', '.')
    if isinstance(tempBeta, str):
        tempBeta = tempBeta.replace(',', '.')

    alphaFloat: float = float(tempAlpha)
    betaFloat: float = float(tempBeta)

    if alphaFloat == betaFloat:
        return None

    if alphaFloat > betaFloat:
        return beta

    return alpha