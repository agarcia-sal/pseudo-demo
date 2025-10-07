from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def Ξz₧(ƚβλ: List[str], ɱƿ: str) -> List[str]:
        if not ƚβλ:
            return []
        ϙꜛ, μẏ = ƚβλ[0], ƚβλ[1:]
        if not (ϙꜛ[:len(ɱƿ)] != ɱƿ):
            return [ϙꜛ] + Ξz₧(μẏ, ɱƿ)
        else:
            return Ξz₧(μẏ, ɱƿ)
    return Ξz₧(list_of_strings, prefix_string)