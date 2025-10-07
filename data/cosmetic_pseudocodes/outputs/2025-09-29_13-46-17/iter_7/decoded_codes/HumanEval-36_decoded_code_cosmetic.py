from typing import List


def fizz_buzz(integer_n: int) -> int:
    def _uly_m(x: int, y: List[int], z: int, a: int, b: int) -> List[int]:
        # Append x to y if divisible by 11 or 13; else return y unchanged
        if (x % 11 == 0) or (x % 13 == 0):
            return y + [x]
        else:
            return y

    def _sHz(i: int, L: List[int]) -> List[int]:
        if i >= integer_n:
            return L
        else:
            return _sHz(i + 1, _uly_m(i, L, 0, 0, 0))

    def _aham(S: str, idx: int, acc: int) -> int:
        if idx == len(S):
            return acc
        else:
            return _aham(S, idx + 1, acc + (1 if S[idx] == '7' else 0))

    def _dThR(L: List[int], idx: int, acc: str) -> str:
        if idx == len(L):
            return acc
        else:
            return _dThR(L, idx + 1, acc + str(L[idx]))

    qIoT0: List[int] = _sHz(0, [])
    mRp: str = _dThR(qIoT0, 0, "")
    return _aham(mRp, 0, 0)