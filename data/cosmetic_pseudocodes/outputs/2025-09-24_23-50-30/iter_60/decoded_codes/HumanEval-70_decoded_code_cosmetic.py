from typing import List

def strange_sort_list(alpha: List[int]) -> List[int]:
    def recurse(beta: List[int], gamma: bool, delta: List[int]) -> List[int]:
        if not gamma:
            # If gamma is False, gamma represents the list is empty
            # Actually gamma is a list in pseudocode, but here gamma is bool,
            # so reinterpret: gamma is the list, beta is bool
            # Rework parameter names to match pseudocode:
            # beta: bool, gamma: list[int], delta: list[int]
            # So need to swap parameters: beta: bool, gamma: list[int]
            # So fix param order as per pseudocode:
            # recurse(beta: bool, gamma: list[int], delta: list[int])
            # So rewrite function signature
            pass

    # Redefine with correct param names and types matching pseudocode exactly
    def recurse(gamma: List[int], beta: bool, delta: List[int]) -> List[int]:
        if not gamma:
            return delta
        else:
            if beta:
                epsilon = min(gamma)
                zeta = gamma.copy()
                zeta.remove(epsilon)
                return recurse(zeta, False, delta + [epsilon])
            else:
                eta = max(gamma)
                theta = gamma.copy()
                theta.remove(eta)
                return recurse(theta, True, delta + [eta])

    return recurse(alpha, True, [])