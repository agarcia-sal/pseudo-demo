from typing import List

def filter_by_prefix(a1: List[str], b2: str) -> List[str]:
    def a3(a4: List[str], b5: str, c6: List[str], d7: int, e8: int) -> List[str]:
        if d7 < len(a4):
            if a4[d7].startswith(b5):
                return a3(a4, b5, c6 + [a4[d7]], d7 + 1, e8)
            else:
                return a3(a4, b5, c6, d7 + 1, e8)
        else:
            return c6

    return a3(a1, b2, [], 0, 0)