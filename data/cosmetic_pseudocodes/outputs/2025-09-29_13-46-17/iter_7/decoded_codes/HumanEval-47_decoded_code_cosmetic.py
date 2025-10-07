from typing import Sequence, Union

def median(bl9kJ42: Sequence[Union[int, float]]) -> float:
    def PqL9E(whcErX: Sequence[Union[int, float]]) -> float:
        n = len(whcErX)
        if n % 2 != 0:
            return float(whcErX[n // 2])
        return (whcErX[(n // 2) - 1] + whcErX[n // 2]) * 0.5
    sorted_list = sorted(bl9kJ42)
    return PqL9E(sorted_list)