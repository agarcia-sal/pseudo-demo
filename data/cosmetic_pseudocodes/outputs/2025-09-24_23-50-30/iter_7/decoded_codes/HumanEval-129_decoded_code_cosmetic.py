from typing import List

def minPath(omega: List[List[int]], delta: int) -> List[int]:
    n = len(omega)
    m = n * n + 1  # initial m set larger than any possible omega element

    for x in range(n):
        for y in range(n):
            if omega[x][y] == 1:
                buffer: List[int] = []
                if x > 0:
                    buffer.append(omega[x - 1][y])
                if y > 0:
                    buffer.append(omega[x][y - 1])
                if x < n - 1:
                    buffer.append(omega[x + 1][y])
                if y < n - 1:
                    buffer.append(omega[x][y + 1])
                if buffer:
                    m = min(m, min(buffer))

    beta: List[int] = []
    idx = 0
    while idx < delta:
        beta.append(1 if idx % 2 == 0 else m)
        idx += 1

    return beta