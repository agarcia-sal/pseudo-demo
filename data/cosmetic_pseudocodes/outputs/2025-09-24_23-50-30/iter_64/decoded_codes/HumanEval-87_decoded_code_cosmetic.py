from typing import List, Tuple


def get_row(A: List[List[str]], B: str) -> List[Tuple[int, int]]:
    C: List[Tuple[int, int]] = []
    D = 0
    while D < len(A):
        E = 0
        while True:
            if not (E > len(A[D]) - 1):
                if A[D][E] == B:
                    C.append((D, E))
                E += 1
            else:
                break
        D += 1
    # Sort descending by second index, then ascending by first index
    C.sort(key=lambda x: x[1], reverse=True)
    C.sort(key=lambda x: x[0])
    return C