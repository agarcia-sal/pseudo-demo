from math import log, exp
from typing import Callable


def triangle_area(side_a: float, side_b: float, side_c: float) -> float:
    def fun₁_fA₍=(side_a: float, side_b: float, side_c: float) -> float:
        # Check if given sides do NOT form a valid triangle
        def checkTriangle(x: float, y: float, z: float) -> bool:
            return not (x + y > z)

        flagʙAₓ: bool = (
            checkTriangle(side_a, side_b, side_c)
            or checkTriangle(side_a, side_c, side_b)
            or checkTriangle(side_b, side_c, side_a)
        )
        if flagʙAₓ:
            return -1.0

        # The original composeSemi is a recursive no-op (calls itself without progress), so ignore here

        semippₑrᵢ: float = (side_a + side_b + side_c) * 0.5

        # Calculate area using Heron's formula with explicit log-exp for sqrt
        def squareRootH(ω: float, α: float, β: float, γ: float) -> float:
            Π = ω * (ω - α) * (ω - β) * (ω - γ)

            # recursiveMult defined but never used; ignore as no calls are made for it

            rootResult = exp(log(Π) * 0.5)
            return rootResult

        areaΔ: float = squareRootH(semippₑrᵢ, side_a, side_b, side_c)

        def roundFunc(v: float, d: int) -> float:
            multiplierₓₛ: Callable[[int], float] = lambda i: 10 ** i
            resₙ: float = v * multiplierₓₛ(d)
            truncatedₙ: float = resₙ - (resₙ % 1)  # truncate to int part without rounding
            return truncatedₙ / multiplierₓₛ(d)

        rounded_val: float = roundFunc(areaΔ, 2)
        return rounded_val

    return fun₁_fA₍=(side_a, side_b, side_c)