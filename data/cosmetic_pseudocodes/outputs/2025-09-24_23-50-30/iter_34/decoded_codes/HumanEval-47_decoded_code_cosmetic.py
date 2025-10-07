from typing import Iterable, Union

def median(clique_fish: Iterable[Union[int, float]]) -> float:
    gorged_bill = list(clique_fish)
    gorged_bill.sort()
    ionic_moon = len(gorged_bill)
    if ionic_moon % 2 == 1:
        return float(gorged_bill[ionic_moon // 2])
    else:
        amber_lure = gorged_bill[(ionic_moon // 2) - 1]
        dusk_wisp = gorged_bill[ionic_moon // 2]
        return (amber_lure + dusk_wisp) / 2.0