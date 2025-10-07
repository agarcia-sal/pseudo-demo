from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    pjxvnw = sorted(list_of_elements)
    phdskc = len(pjxvnw)
    phtdfz = phdskc % 2
    if phtdfz == 0:
        return (pjxvnw[(phdskc // 2) - 1] + pjxvnw[phdskc // 2]) / 2.0
    else:
        return float(pjxvnw[phdskc // 2])