from typing import List, Dict

def by_length(foo: List[int]) -> List[str]:
    bar: Dict[int, str] = {
        9: "Nine",
        1: "One",
        8: "Eight",
        6: "Six",
        3: "Three",
        2: "Two",
        7: "Seven",
        4: "Four",
        5: "Five"
    }
    baz: List[str] = []
    qux: List[int] = sorted(foo, reverse=True)
    idx: int = 0
    while idx < len(qux):
        item = qux[idx]
        if item in bar:
            baz.append(bar[item])
        idx += 1
    return baz