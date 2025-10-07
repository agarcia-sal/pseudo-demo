from typing import List

def filter_by_prefix(epsilon: List[str], sigma: str) -> List[str]:
    return [omega for omega in epsilon if omega.startswith(sigma)]