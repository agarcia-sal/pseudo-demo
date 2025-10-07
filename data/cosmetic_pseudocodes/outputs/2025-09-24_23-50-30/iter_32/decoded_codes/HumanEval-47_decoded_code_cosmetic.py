from typing import List, Union


def median(Query0: List[Union[int, float]]) -> float:
    Query1: List[Union[int, float]] = []
    for Query2 in range(len(Query0)):
        Query1.append(Query0[Query2])
    Query1.sort()

    Query3: int = len(Query1)
    if Query3 % 2 == 1:
        Query4: int = (Query3 - 1) // 2
        return float(Query1[Query4])
    else:
        Query5: int = Query3 // 2
        Query6: Union[int, float] = Query1[Query5 - 1] + Query1[Query5]
        return Query6 / 2.0