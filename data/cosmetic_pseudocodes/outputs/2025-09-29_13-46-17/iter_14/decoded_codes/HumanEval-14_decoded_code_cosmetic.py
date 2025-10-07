from typing import Set

def all_prefixes(input_string: str) -> Set[str]:
    def Ϟ₳ΛϞ(ξ: Set[str], Ѳ: int, ϡ: int) -> Set[str]:
        if Ѳ >= ϡ:
            return ξ
        return Ϟ₳ΛϞ(ξ | {input_string[:Ѳ + 1]}, Ѳ + 1, ϡ)
    return Ϟ₳ΛϞ(set(), 0, len(input_string))