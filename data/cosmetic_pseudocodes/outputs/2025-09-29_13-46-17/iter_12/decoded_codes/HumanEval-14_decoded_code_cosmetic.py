from typing import List

def all_prefixes(input_string: str) -> List[str]:
    def Ψ(κ0: int, αβγ: List[str]) -> List[str]:
        if κ0 >= len(input_string):
            return αβγ
        return Ψ(κ0 + 1, αβγ + [input_string[:κ0 + 1]])
    return Ψ(0, [])