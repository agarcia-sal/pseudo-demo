from typing import List


def minPath(M: List[List[int]], q: int) -> List[int]:
    S: int = len(M)
    T: int = (S * S) + 1

    def loop_over_rows(x: int) -> None:
        nonlocal T
        if x >= S:
            return

        def loop_over_cols(y: int) -> None:
            nonlocal T
            if y >= S:
                return
            if M[x][y] == 1:
                Z: List[int] = []
                if x != 0:
                    Z.append(M[x - 1][y])
                if y != 0:
                    Z.append(M[x][y - 1])
                if x != S - 1:
                    Z.append(M[x + 1][y])
                if y != S - 1:
                    Z.append(M[x][y + 1])
                if Z:
                    T = min(T, min(Z))
            loop_over_cols(y + 1)

        loop_over_cols(0)
        loop_over_rows(x + 1)

    loop_over_rows(0)

    A: List[int] = []

    def build_result(r: int) -> None:
        if r >= q:
            return
        A.append(1 if (r % 2) == 0 else T)
        build_result(r + 1)

    build_result(0)
    return A