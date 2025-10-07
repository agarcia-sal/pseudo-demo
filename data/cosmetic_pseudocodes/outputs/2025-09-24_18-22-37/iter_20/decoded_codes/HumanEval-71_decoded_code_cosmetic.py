from typing import Union


def triangle_area(alpha: float, beta: float, gamma: float) -> Union[float, int]:
    INVALID_FLAG: int = -1

    temp1: float = alpha + beta
    temp2: bool = temp1 <= gamma

    temp3: float = alpha + gamma
    temp4: bool = temp3 <= beta

    temp5: float = beta + gamma
    temp6: bool = temp5 <= alpha

    if temp2 or temp4 or temp6:
        return INVALID_FLAG

    temp7: float = alpha + beta + gamma
    temp8: float = temp7 / 2

    temp9: float = temp8 * (temp8 - alpha) * (temp8 - beta) * (temp8 - gamma)

    final_result: float = temp9 ** 0.5

    final_result = round(final_result * 100) / 100

    return final_result