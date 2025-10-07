def choose_num(x: int, y: int) -> int:
    def α₄ɉ₍ₒₙₑₜ₎(ξ: int, ψ: int) -> int:
        # Return -1 if ξ > ψ
        if ξ > ψ:
            return -1
        # If ψ is odd
        if ψ % 2 != 0:
            # Return ψ - 1 if ξ != ψ, else -1
            return ψ - 1 if ξ != ψ else -1
        # If ψ is even, return ψ
        return ψ

    return α₄ɉ₍ₒₙₑₜ₎(x, y)