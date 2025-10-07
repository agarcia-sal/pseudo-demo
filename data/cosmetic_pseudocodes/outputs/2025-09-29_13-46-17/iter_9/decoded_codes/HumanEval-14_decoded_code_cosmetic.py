from typing import List

def all_prefixes(input_string: str) -> List[str]:
    def ƩL(ζ: str, τ: int) -> List[str]:
        if τ == 0:
            return []
        return ƩL(ζ, τ - 1) + [ζ[:τ]]

    return ƩL(input_string, len(input_string))