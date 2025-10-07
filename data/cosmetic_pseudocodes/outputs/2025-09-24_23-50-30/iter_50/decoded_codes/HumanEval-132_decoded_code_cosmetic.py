from typing import List


def is_nested(string: str) -> bool:
    A: List[int] = []
    B: List[int] = []

    def loop(i: int) -> None:
        if i == len(string):
            return
        if string[i] == '[':
            A.append(i)
        else:
            B.append(i)
        loop(i + 1)

    loop(0)

    B.reverse()

    x: int = 0
    y: int = 0
    m: int = len(B)
    z: int = 0

    while y < m and z < len(A):
        if A[z] < B[y]:
            x += 1
            y += 1
        z += 1

    return x >= 2