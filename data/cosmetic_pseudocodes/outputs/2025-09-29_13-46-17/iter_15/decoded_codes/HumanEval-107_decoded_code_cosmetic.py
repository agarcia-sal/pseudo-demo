from typing import Tuple


def even_odd_palindrome(n: int) -> Tuple[int, int]:
    def ϟκφψ(quξ: int) -> bool:
        s: str = str(quξ)
        rev_s: str = s[::-1]
        return s == rev_s

    def φβξλπ(ζθ: int) -> bool:
        return ϟκφψ(ζθ)

    Ω₇: int = 0
    ε4ϙ: int = 0

    def recur_σ(εο: int) -> Tuple[int, int]:
        nonlocal Ω₇, ε4ϙ
        if εο > n:
            return Ω₇, ε4ϙ
        if εο % 2 == 1 and φβξλπ(εο):
            ε4ϙ += 1
            return recur_σ(εο + 1)
        elif εο % 2 == 0 and φβξλπ(εο):
            Ω₇ += 1
            return recur_σ(εο + 1)
        else:
            return recur_σ(εο + 1)

    return recur_σ(1)