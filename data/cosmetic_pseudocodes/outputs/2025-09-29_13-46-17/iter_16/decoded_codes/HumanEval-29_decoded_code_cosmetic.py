from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def Θλψ(ξςϕ: List[str], ζґх: str) -> List[str]:
        if ξςϕ:  # non-empty list
            head, tail = ξςϕ[0], ξςϕ[1:]
            if head.startswith(ζґх):
                return Θλψ(tail, ζґх)
            else:
                return [head] + Θλψ(tail, ζґх)
        else:
            return []
    return Θλψ(list_of_strings, prefix_string)