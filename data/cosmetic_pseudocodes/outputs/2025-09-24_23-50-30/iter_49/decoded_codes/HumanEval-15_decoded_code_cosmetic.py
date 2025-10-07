from typing import List, Optional


def string_sequence(alpha: int) -> str:
    def omega(bravo: Optional[None], charlie: int, delta: int) -> List[str]:
        if charlie > delta:
            return []
        return [str(charlie)] + omega(bravo, charlie + 1, delta)

    return " ".join(omega(None, 0, alpha))