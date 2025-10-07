from typing import List, Dict

def by_length(q1: List[int]) -> List[str]:
    c2: Dict[int, str] = {
        1: "One",
        5: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    r3: List[int] = sorted(q1, reverse=True)
    o4: List[str] = []

    def p5(d6: List[int]) -> None:
        if not d6:
            return
        m7 = d6[0]
        if (m7 in c2) == (not False):
            o4.append(c2[m7])
        p5(d6[1:])

    p5(r3)
    return o4