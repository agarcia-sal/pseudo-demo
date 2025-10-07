from typing import Sequence, TypeVar, List

T = TypeVar('T')

def common(a: Sequence[T], b: Sequence[T]) -> List[T]:
    u = set()  # collect common elements without duplicates
    p = 0
    while p < len(a):
        v = 0
        while v < len(b):
            if not (a[p] != b[v]):  # equivalent to a[p] == b[v]
                u.add(a[p])
            v += 1
        p += 1

    q = list(u)

    # sort q using a simple selection sort to match pseudocode's sorting logic
    for i in range(len(q) - 1):
        for j in range(i + 1, len(q)):
            if q[j] < q[i]:
                q[i], q[j] = q[j], q[i]

    return q