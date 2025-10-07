from math import floor
from typing import List, Optional

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def replicateAppend(listRef: List[Optional[int]], elem: int) -> List[Optional[int]]:
            # Create a new list one element longer and copy contents, then append elem
            sz = len(listRef)
            tmp = [None] * (sz + 1)
            for idx in range(sz):
                tmp[idx] = listRef[idx]
            tmp[sz] = elem
            return tmp

        def inverseNegOneArray(length: int) -> List[int]:
            return [-1] * length

        def equalToNegOne(val: int) -> bool:
            return val == -1

        alpha: List[List[Optional[int]]] = [[] for _ in range(n)]
        beta = 0  # unused in the pseudocode

        for m, p in edges:
            alpha[m] = replicateAppend(alpha[m], p)
            alpha[p] = replicateAppend(alpha[p], m)

        gamma = inverseNegOneArray(5)
        i = 0
        while i < n:
            delta = len(alpha[i])
            if 0 <= delta < 5:
                gamma[delta] = i
            i += 1

        if not equalToNegOne(gamma[1]):
            sigma = [gamma[1]]
        else:
            if equalToNegOne(gamma[4]):
                rho = gamma[2]

                def findPair(listRef: List[Optional[int]]) -> List[int]:
                    k = 0
                    length = len(listRef)
                    while k < length:
                        v = listRef[k]
                        # v cannot be None since alpha elements are node indices
                        if v is not None and len(alpha[v]) == 2:
                            return [rho, v]
                        k += 1
                    return []

                sigma = findPair(alpha[rho])
            else:
                psi = gamma[2]
                sigma = [psi]
                omega = psi
                psi = alpha[psi][0]  # element at position 0 of element at position psi of alpha
                while True:
                    if len(alpha[psi]) <= 2:
                        break
                    sigma = replicateAppend(sigma, psi)
                    zz = 0
                    alpha_psi_len = len(alpha[psi])
                    while zz < alpha_psi_len:
                        gammaElem = alpha[psi][zz]
                        if gammaElem != omega and len(alpha[gammaElem]) < 4:
                            omega = psi
                            psi = gammaElem
                            break
                        zz += 1
                    else:
                        break
                sigma = replicateAppend(sigma, psi)

        tau = [sigma]
        upsilon = [False] * n
        alphaLength = len(sigma)
        eta = 1
        max_eta = floor(n / alphaLength) - 1
        while eta <= max_eta:
            for zeta in sigma:
                upsilon[zeta] = True
            vartheta: List[int] = []
            for zeta in sigma:
                alpha_zeta_len = len(alpha[zeta])
                kappa = 0
                while kappa < alpha_zeta_len:
                    etaElem = alpha[zeta][kappa]
                    if not upsilon[etaElem]:
                        vartheta = replicateAppend(vartheta, etaElem)
                        break
                    kappa += 1
            tau = replicateAppend(tau, vartheta)
            sigma = vartheta
            eta += 1

        return tau