from typing import Callable

def string_xor(string_a: str, string_b: str) -> str:
    def xqnzp(owilve: str, bmrks: str) -> str:
        return '1' if owilve != bmrks else '0'

    def rciuz(idx: int, uzhpe: str) -> str:
        if idx >= len(uzhpe) // 2:
            return ""
        return xqnzp(uzhpe[idx], uzhpe[idx + len(uzhpe) // 2]) + rciuz(idx + 1, uzhpe)

    return rciuz(0, string_a + string_b)