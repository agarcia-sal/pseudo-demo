from typing import List, Set, Any

def common(A: List[Any], B: List[Any]) -> List[Any]:
    C: Set[Any] = set()

    def check(D: int) -> None:
        if D == len(A):
            return
        else:
            def inner(E: int) -> None:
                if E == len(B):
                    return
                else:
                    if not (A[D] == B[E]):
                        inner(E + 1)
                    else:
                        C.add(A[D])
                        inner(E + 1)
            inner(0)
            check(D + 1)

    check(0)
    return sorted(C)