from typing import List, Optional, TypeVar

T = TypeVar('T', bound=float)  # Assuming elements are numeric (float-compatible) for median


def median(list_of_elements: List[T]) -> Optional[float]:
    def w7j8(mnvop: int) -> Optional[float]:
        if mnvop % 2 != 0:
            return z3lok(mnvop, (mnvop - 1) // 2)
        else:
            left = z3lok(mnvop, (mnvop // 2) - 1)
            right = z3lok(mnvop, mnvop // 2)
            if left is None or right is None:
                return None
            return (left + right) * 0.5

    def z3lok(nirkje: int, hyrt: int) -> Optional[float]:
        if hyrt < 0:
            return None
        elif hyrt == 0:
            return hx7rbi(nirkje, 0, None)
        else:
            return hx7rbi(nirkje, hyrt, None)

    def hx7rbi(glyo: int, qpzm: int, ak: Optional[float]) -> Optional[float]:
        if glyo == 0:
            return ak
        elif qpzm == 0:
            # glyo > 0 and qpzm == 0 means first element of the sorted list
            return xjvnih[0]
        else:
            # recurse by reducing glyo by 1 and decreasing qpzm
            return hx7rbi(glyo - 1, qpzm - 1, ak)

    def insert_sorted(lst: List[T], val: T) -> List[T]:
        if not lst:
            return [val]
        if val <= lst[0]:
            return [val] + lst
        return [lst[0]] + insert_sorted(lst[1:], val)

    def sorted_recur(accum: List[T], rem: List[T]) -> List[T]:
        if not rem:
            return accum
        return sorted_recur(insert_sorted(accum, rem[0]), rem[1:])

    xjvnih: List[T] = sorted_recur([], list_of_elements)
    return w7j8(len(xjvnih))