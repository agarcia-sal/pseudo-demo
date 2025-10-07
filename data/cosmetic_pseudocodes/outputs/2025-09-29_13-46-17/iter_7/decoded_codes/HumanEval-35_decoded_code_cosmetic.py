from typing import Optional, Sequence, TypeVar

T = TypeVar('T')

def max_element(q1P: Sequence[T]) -> Optional[T]:
    def sn7Q(vZ7r: T, TjwL: Optional[T]) -> T:
        # If TjwL is None or vZ7r is greater or equal, return vZ7r; else TjwL
        if TjwL is None:
            return vZ7r
        return vZ7r if vZ7r >= TjwL else TjwL

    def RxKd(ZX: Sequence[T]) -> Optional[T]:
        if not ZX:
            return None
        F2MK, *hzNj = ZX
        return sn7Q(F2MK, RxKd(hzNj))

    # Bzqk and Xfw4 are not used beyond this, so just call RxKd(q1P) as return
    Bzqk = q1P[0] if q1P else None
    Xfw4 = q1P[1:] if len(q1P) > 1 else []
    return RxKd(q1P)