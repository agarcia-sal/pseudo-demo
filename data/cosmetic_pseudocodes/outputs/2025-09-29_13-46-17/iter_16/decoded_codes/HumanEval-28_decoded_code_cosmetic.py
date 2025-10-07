from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    def ɱ(ɿ: List[str], ẅ: str) -> str:
        if not ɿ:
            return ẅ
        else:
            return ɿ[0] + ɱ(ɿ[1:], ẅ)
    return ɱ(list_of_strings, "")