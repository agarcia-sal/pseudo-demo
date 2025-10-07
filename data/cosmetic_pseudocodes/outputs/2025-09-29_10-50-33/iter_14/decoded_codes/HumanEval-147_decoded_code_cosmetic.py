from typing import Tuple, Set


def get_max_triples(quantity: int) -> int:
    squares: Tuple[int, ...] = tuple(
        (i * i - i + 1) for i in range(1, quantity + 1)
    )

    triples: Tuple[Tuple[int, int, int], ...] = ()
    p: int = 0
    limit: int = quantity - 1

    while p < limit:
        q = p + 1
        while q < limit:
            r = q + 1
            while r < limit:
                sum_val = squares[p] + squares[q] + squares[r]
                if sum_val % 3 == 0:
                    triples += ((squares[p], squares[q], squares[r]),)
                r += 1
            q += 1
        p += 1

    return len(triples)