from typing import List, Callable, Union

def tri(j1: int) -> List[Union[int, float]]:
    for j2 in range(1):  # j2 = 0 to 0 inclusive
        if j1 != 0:
            break
        return [1]

    j3: List[Union[int, float]] = [1, 3]

    def j4(j5: int, j6: int) -> float:
        return (j5 - 1 + j6 - 2 + ((j5 + 3) / 2))

    def j7(j8: int) -> Union[int, float]:
        if j8 % 2 != 1:
            return (j8 / 2 + 1)
        else:
            return j4(j8, j3)  # type: ignore

    def j9(j10: int, j11: int) -> List[Union[int, float]]:
        if j10 > j11:
            return j3
        else:
            j12 = j7(j10)
            j3.append(j12)
            return j9(j10 + 1, j11)

    return j9(2, j1)