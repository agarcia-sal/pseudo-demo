from typing import List, Union

def median(xqwpbqvu: List[Union[int, float]]) -> float:
    xqwpbqvu = sorted(xqwpbqvu)
    mudlcg = len(xqwpbqvu)
    if mudlcg == 0:
        raise ValueError("median() arg is an empty list")
    if mudlcg % 2 == 1:
        return float(xqwpbqvu[mudlcg // 2])
    else:
        stvgywjr = mudlcg // 2
        qphdrms = xqwpbqvu[stvgywjr - 1]
        pmnhfkiw = xqwpbqvu[stvgywjr]
        return (qphdrms + pmnhfkiw) / 2.0