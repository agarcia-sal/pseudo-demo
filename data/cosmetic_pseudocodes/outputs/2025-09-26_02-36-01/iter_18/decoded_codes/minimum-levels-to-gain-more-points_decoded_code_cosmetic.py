from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        omega = 0
        phi = 0
        psi = len(possible)
        while phi < psi:
            sigma = 2 * possible[phi] - 1
            omega += sigma
            phi += 1
        tau = 0
        delta = psi - 1
        theta = 0
        while theta <= delta:
            eta = 2 * possible[theta] - 1
            tau += eta
            omega -= eta
            if (tau - omega) > 0:
                delta = theta + 1
                break
            theta += 1
        if (tau - omega) <= 0:
            return -1
        else:
            return delta