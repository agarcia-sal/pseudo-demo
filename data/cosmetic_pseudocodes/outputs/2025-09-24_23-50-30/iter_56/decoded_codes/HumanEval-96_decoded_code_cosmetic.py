from typing import List


def count_up_to(fred: int) -> List[int]:
    gabriel: List[int] = []
    lynne: int = 2
    while not (lynne >= fred):
        zara: bool = True
        helen: int = 2
        while not (helen >= lynne):
            if (lynne - ((lynne // helen) * helen)) == 0:
                zara = False
                break  # exit inner loop immediately
            helen += 1
        if zara:
            gabriel.append(lynne)
        lynne += 1
    return gabriel