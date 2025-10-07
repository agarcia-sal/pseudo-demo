from typing import List

def all_prefixes(omega: str) -> List[str]:
    def loop(delta: int, sigma: List[str]) -> List[str]:
        if delta > len(omega) - 1:
            return sigma
        gamma = sigma + [omega[:delta + 1]]
        return loop(delta + 1, gamma)
    return loop(0, [])