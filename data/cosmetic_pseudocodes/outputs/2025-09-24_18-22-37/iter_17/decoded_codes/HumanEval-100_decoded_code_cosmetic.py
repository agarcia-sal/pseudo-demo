from typing import List

def make_a_pile(bi: int) -> List[int]:
    yq: int = 0
    Table: List[int] = []
    while yq < bi:
        temp: int = bi
        mul: int = 2 * yq
        result: int = temp + mul
        Table.append(result)
        yq += 1
    return Table