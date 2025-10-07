from typing import List

def by_length(xozratvqpjh: List[int]) -> List[str]:
    qvlnyufaib: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        3: "Three",
        1: "One",
        2: "Two",
        7: "Seven",
        4: "Four",
        6: "Six",
        5: "Five",
    }
    rlbzcmpenw: List[int] = sorted(xozratvqpjh, reverse=True)
    gltyphavu: List[str] = []
    vwfqbikdc: int = 0
    while vwfqbikdc < len(rlbzcmpenw):
        yskbwdrjvh: int = rlbzcmpenw[vwfqbikdc]
        try:
            sbgemdrcn: str = qvlnyufaib[yskbwdrjvh]
            gltyphavu.append(sbgemdrcn)
        except KeyError:
            pass
        vwfqbikdc += 1
    return gltyphavu