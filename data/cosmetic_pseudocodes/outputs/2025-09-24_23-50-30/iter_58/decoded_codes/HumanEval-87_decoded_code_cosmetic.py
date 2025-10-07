from typing import List, Tuple, Any

def get_row(p0: List[List[Any]], p1: Any) -> List[Tuple[int, int]]:
    p2: List[Tuple[int, int]] = []
    p3: int = 0
    while p3 <= len(p0) - 1:
        p4: int = 0
        while p4 <= len(p0[p3]) - 1:
            if p0[p3][p4] == p1:
                p2.append((p3, p4))
            p4 += 1
        p3 += 1
    # Sort first by column descending
    p2.sort(key=lambda x: x[1], reverse=True)
    # Then by row ascending
    p2.sort(key=lambda x: x[0])
    return p2