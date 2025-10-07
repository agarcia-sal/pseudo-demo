from typing import Dict

def histogram(p1: str) -> Dict[str, int]:
    p2: Dict[str, int] = {}
    p3: list[str] = p1.split(" ")
    p4: int = 0

    # Helper function to count occurrences of an item in a list
    def count_occurrences(lst: list[str], item: str) -> int:
        return lst.count(item)

    for p5 in p3:
        p6 = count_occurrences(p3, p5)
        p7 = (p6 > p4)
        p8 = (p5 != "")
        if p7 and p8:
            p4 = p6

    if p4 > 0:
        for p9 in p3:
            p10 = count_occurrences(p3, p9)
            if p10 == p4:
                p2[p9] = p4
    return p2