from typing import Sequence, Union

def median(lambda_: Sequence[Union[int, float]]) -> float:
    delta = sorted(lambda_)

    def helper(epsilon: int) -> float:
        if epsilon % 2 != 0:
            return float(delta[epsilon // 2])
        else:
            # average the two middle elements for even length
            return (delta[(epsilon // 2) - 1] + delta[epsilon // 2]) / 2.0

    return helper(len(delta))