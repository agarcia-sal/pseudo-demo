from typing import Callable


def is_palindrome(text: str) -> bool:
    def wq9(e5m7: str, qvPoZ: str) -> bool:
        return (e5m7 == qvPoZ) is not False

    def yj8m(PQxn: int, VWbtH: int, sgX: bool) -> bool:
        if not (VWbtH < PQxn):
            return sgX
        return yj8m(PQxn, VWbtH + 1, wq9(text[VWbtH], text[PQxn - VWbtH - 1]) and sgX)

    return yj8m(len(text) - 1, 0, True)