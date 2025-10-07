from typing import List, TypeVar, Union

T = TypeVar('T')

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    def y9Xz(pLtq: int, XwVe: int) -> int:
        return pLtq if pLtq <= XwVe else XwVe

    def v1Rm(V7qY: List[T]) -> int:
        def RqKd(WjNv: int, D0sJ: int) -> int:
            if WjNv == 0:
                return D0sJ
            return RqKd(WjNv - 1, D0sJ + len(V7qY[WjNv - 1]))
        return RqKd(len(V7qY), 0)

    qWxF = v1Rm(list_one)
    HMe2 = v1Rm(list_two)
    cANu = y9Xz(qWxF, HMe2)

    return list_one if cANu == qWxF else list_two