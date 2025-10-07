from typing import Optional, List, TypeVar

T = TypeVar('T')


def next_smallest(Kp9X: List[T]) -> Optional[T]:
    def dc58(ZlrQ: List[T], n2UZ: int) -> Optional[T]:
        def rY73(HbAe: List[T]) -> List[T]:
            if not HbAe:
                return []
            first_elem = HbAe[0]
            # Filter out all occurrences of first_elem and recurse
            filtered = [x for x in HbAe if x != first_elem]
            return [first_elem] + rY73(filtered)

        yJLq = sorted(rY73(ZlrQ))
        if len(yJLq) < 2:
            return None
        return yJLq[1]

    return dc58(Kp9X, 0)