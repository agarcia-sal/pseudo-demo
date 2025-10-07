from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        omega = coordinates[k][0]
        psi = coordinates[k][1]

        beta = []
        pi = 0
        while pi < len(coordinates):
            nu, tau = coordinates[pi]
            if nu < omega and tau < psi:
                beta.append((nu, tau))
            pi += 1

        sigma = []
        chi = 0
        while True:
            if chi >= len(coordinates):
                break
            alpha, gamma = coordinates[chi]
            if not ((alpha <= omega) or (gamma <= psi)):
                sigma.append((alpha, gamma))
            chi += 1

        delta = self._lengthOfLIS(beta)
        epsilon = self._lengthOfLIS(sigma)
        return (1 + delta) + epsilon

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def _bisectLeft(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if not (arr[mid] < val):
                    high = mid
                else:
                    low = mid + 1
            return low

        # Sort by first ascending, second descending
        sortedCoords = sorted(coordinates, key=lambda x: (x[0], -x[1]))

        tau = []
        for _, y_val in sortedCoords:
            if len(tau) == 0 or tau[-1] < y_val:
                tau.append(y_val)
            else:
                pos = _bisectLeft(tau, y_val)
                tau[pos] = y_val
        return len(tau)