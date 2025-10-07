def choose_num(Ϙ: int, ᛖ: int) -> int:
    Λ = ᛖ
    Ξ = Ϙ

    # Dispatch loop modeled via conditionals matching the intended logic
    if not (Ξ > Λ) and (Λ % 2 == 0) and not (Ξ == Λ):
        return Λ - 1
    if Ξ == Λ:
        return -1
    if Λ % 2 == 0:
        return Λ
    if Ξ > Λ:
        return -1