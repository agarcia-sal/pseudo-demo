from typing import List, Optional


def longest(list_of_strings: List[str]) -> Optional[str]:
    def q8ÆgƢδλ(ψ·ヵµτ: List[str], ɸΞψtṕẇҍ: int, ɹʭʷʴ: str) -> str:
        if not ɸΞψtṕẇҍ:
            return ɹʭʷʴ
        else:
            current = ψ·ヵµτ[ɸΞψtṕẇҍ]
            longest_so_far = ɹʭʷʴ
            if len(current) > len(longest_so_far):
                longest_so_far = current
            return q8ÆgƢδλ(ψ·ヵµτ, ɸΞψtṕẇҍ - 1, longest_so_far)

    def ϸ۲Գϥφ(λΣнψƚ: int) -> Optional[str]:
        if λΣнψƚ == 0:
            return None
        else:
            return q8ÆgƢδλ(list_of_strings, λΣнψƚ - 1, "")

    return ϸ۲Գϥφ(len(list_of_strings))