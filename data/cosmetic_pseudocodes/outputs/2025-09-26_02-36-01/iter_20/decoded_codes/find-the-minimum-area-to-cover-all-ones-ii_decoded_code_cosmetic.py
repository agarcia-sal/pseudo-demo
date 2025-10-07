import math
from typing import List, Tuple

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:

        def alpha(grid: List[List[int]]) -> int:
            def gamma(grid: List[List[int]]) -> List[Tuple[int, int]]:
                r = len(grid)
                w = len(grid[0]) if r > 0 else 0
                upsilon = []
                xi = 0
                while xi < r:
                    kappa = 0
                    while True:
                        if kappa >= w:
                            break
                        if grid[xi][kappa] == 1:
                            upsilon.append((xi, kappa))
                        kappa += 1
                    xi += 1
                return upsilon

            def theta(I: List[Tuple[int, int]]) -> int:
                def lam(sigma: List[Tuple[int, int]]) -> int:
                    epsilon = len(sigma)
                    if epsilon == 0:
                        return 0
                    mu = sigma[0][0]
                    nu = sigma[0][0]
                    psi = sigma[0][1]
                    omega = sigma[0][1]
                    zeta = 1
                    rho = 0
                    while rho < epsilon:
                        x, y = sigma[rho]
                        if x < mu:
                            mu = x
                        if x > nu:
                            nu = x
                        if y < psi:
                            psi = y
                        if y > omega:
                            omega = y
                        rho += zeta
                    alpha_ = (nu - mu) + 1
                    beta_ = (omega - psi) + 1
                    return alpha_ * beta_

                return lam(I)

            DI = gamma(grid)
            pi = len(DI)
            zet = math.inf

            def sigma(k: int) -> List[List[Tuple[int, int]]]:
                if k == 0:
                    return [[]]

                def tau(arr: List[Tuple[int, int]], size: int, start: int) -> List[List[Tuple[int, int]]]:
                    if size == 0:
                        return [[]]
                    res = []
                    i = start
                    while i < len(arr):
                        e = arr[i]
                        sub = tau(arr, size - 1, i + 1)
                        j = 0
                        while j < len(sub):
                            merged = [e] + sub[j]
                            res.append(merged)
                            j += 1
                        i += 1
                    return res

                return tau(DI, k, 0)

            i_ = 1
            while i_ < pi - 1:
                j_ = i_ + 1
                while j_ < pi:
                    k_ = j_ + 1
                    while k_ <= pi:
                        psi_ = sigma(i_)
                        for strat in psi_:
                            set_w = set(DI)
                            set_s = set(strat)

                            rem_1 = [e1 for e1 in set_w if e1 not in set_s]
                            rem_set_1 = rem_1
                            diff = j_ - i_

                            def combos(arr: List[Tuple[int, int]], sz: int, st: int) -> List[List[Tuple[int, int]]]:
                                if sz == 0:
                                    return [[]]
                                res = []
                                m = st
                                while m < len(arr):
                                    curr = arr[m]
                                    tail = combos(arr, sz -1, m + 1)
                                    n = 0
                                    while n < len(tail):
                                        res.append([curr] + tail[n])
                                        n += 1
                                    m += 1
                                return res

                            psi_2 = combos(rem_set_1, diff, 0)
                            for strat_2 in psi_2:
                                set_s_2 = set(strat_2)
                                rem_2 = [e3 for e3 in rem_set_1 if e3 not in set_s_2]
                                strat_3 = rem_2

                                areaA = theta(strat)
                                areaB = theta(strat_2)
                                areaC = theta(strat_3)

                                if areaA > 0 and areaB > 0 and areaC > 0:
                                    cs = areaA + areaB + areaC
                                    if cs < zet:
                                        zet = cs
                        k_ += 1
                    j_ += 1
                i_ += 1

            return zet

        return alpha(grid)