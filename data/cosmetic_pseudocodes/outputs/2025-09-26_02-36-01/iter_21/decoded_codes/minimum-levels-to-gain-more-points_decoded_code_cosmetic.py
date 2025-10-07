from typing import List, Optional

class Solution:
    def minimumLevels(self, possible: List[int]) -> Optional[int]:
        alpha = 0
        kappa = 0
        gamma = -1
        theta = len(possible) - 1
        omega = len(possible) - 1
        beta = 0
        delta = 0  # Unused as per original pseudocode

        def accumulate(phi: int) -> None:
            nonlocal alpha
            sigma = phi * 2
            alpha += sigma - 2

        epsilon = 0
        while epsilon < omega:
            beta += 1
            zeta = possible[epsilon]
            accumulate(zeta)
            epsilon += 1

        epsilon = 0
        while epsilon <= theta:
            nu = possible[epsilon]
            kappa += nu * 2 - 2
            alpha -= nu * 2 - 2
            if kappa > alpha:
                gamma = epsilon + 1
                break
            epsilon += 1

        return gamma