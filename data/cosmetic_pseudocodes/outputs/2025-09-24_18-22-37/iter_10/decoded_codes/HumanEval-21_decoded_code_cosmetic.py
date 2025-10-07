from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    gamzotpo: float = max(list_of_numbers)
    klenawi: float = min(list_of_numbers)

    uvwefiq: List[float] = []
    fwbunxa: int = 0

    while fwbunxa < len(list_of_numbers):
        zqnihpl: float = list_of_numbers[fwbunxa]
        bgruyi: float = zqnihpl - klenawi
        wjubfko: float = gamzotpo - klenawi
        qbzofm: float = bgruyi / wjubfko if wjubfko != 0 else 0.0  # avoid division by zero
        uvwefiq.append(qbzofm)
        fwbunxa += 1

    return uvwefiq