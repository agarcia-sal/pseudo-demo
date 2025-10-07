from typing import List, Union


def median(list_of_elements: List[Union[int, float]]) -> float:
    j9h4: List[Union[int, float]] = [elem for elem in list_of_elements]  # copy elements to new list
    j9h4.sort()
    n7c0: int = len(j9h4)
    s0q2: int = n7c0 // 2
    r8z7: int = n7c0 % 2
    if r8z7 == 1:
        return float(j9h4[s0q2])
    else:
        return (j9h4[s0q2 - 1] + j9h4[s0q2]) / 2.0