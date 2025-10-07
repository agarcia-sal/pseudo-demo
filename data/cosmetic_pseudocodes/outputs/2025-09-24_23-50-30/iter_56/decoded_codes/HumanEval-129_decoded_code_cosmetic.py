from typing import List


def minPath(grid: List[List[int]], beta: int) -> List[int]:
    n: int = len(grid)
    omega: int = (n * n) + 1

    for H_loop_i in range(n):
        for K_loop_j in range(n):
            if grid[H_loop_i][K_loop_j] == 1:
                Delta: List[int] = []
                if H_loop_i != 0:
                    Delta.append(grid[H_loop_i - 1][K_loop_j])
                if K_loop_j != 0:
                    Delta.append(grid[H_loop_i][K_loop_j - 1])
                if H_loop_i != n - 1:
                    Delta.append(grid[H_loop_i + 1][K_loop_j])
                if K_loop_j != n - 1:
                    Delta.append(grid[H_loop_i][K_loop_j + 1])
                if Delta:
                    omega = min(Delta)

    ans_array: List[int] = []
    for U_idx in range(beta):
        flag = (U_idx % 2) == 0
        ans_array.append(1 if flag else omega)

    return ans_array