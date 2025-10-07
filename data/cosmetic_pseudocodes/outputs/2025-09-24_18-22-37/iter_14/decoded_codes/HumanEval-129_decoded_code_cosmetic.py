from typing import List


def minPath(grid: List[List[int]], omega: int) -> List[int]:
    alpha: int = len(grid)
    psi: int = alpha * alpha + 1

    lambda_: int = 0
    while lambda_ < alpha:
        mu: int = 0
        while mu < alpha:
            if grid[lambda_][mu] == 1:
                epsilon_list: List[int] = []

                if lambda_ != 0:
                    epsilon_list.append(grid[lambda_ - 1][mu])
                if mu != 0:
                    epsilon_list.append(grid[lambda_][mu - 1])
                if lambda_ != alpha - 1:
                    epsilon_list.append(grid[lambda_ + 1][mu])
                if mu != alpha - 1:
                    epsilon_list.append(grid[lambda_][mu + 1])

                if epsilon_list:
                    psi = min(epsilon_list)
            mu += 1
        lambda_ += 1

    theta_list: List[int] = []
    nu: int = 0
    while nu < omega:
        remainder_val: int = nu % 2
        if remainder_val == 0:
            theta_list.append(1)
        else:
            theta_list.append(psi)
        nu += 1

    return theta_list