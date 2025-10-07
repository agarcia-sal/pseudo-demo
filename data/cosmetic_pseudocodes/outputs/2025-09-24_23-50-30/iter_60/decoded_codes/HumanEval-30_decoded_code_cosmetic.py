from typing import List

def get_positive(alpha: List[int]) -> List[int]:
    def inner_filter(bravo: List[int], charlie: int) -> List[int]:
        if charlie == len(bravo):
            return []
        if bravo[charlie] > 0:
            return [bravo[charlie]] + inner_filter(bravo, charlie + 1)
        return inner_filter(bravo, charlie + 1)

    return inner_filter(alpha, 0)