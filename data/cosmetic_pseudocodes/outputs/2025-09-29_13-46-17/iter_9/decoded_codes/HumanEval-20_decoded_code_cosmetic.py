from typing import List, Optional, Tuple


def find_closest_elements(arr: List[int]) -> Optional[Tuple[int, int]]:
    # Nested helper functions capturing the pseudocode structure with inferred types.

    def λ(i: int, u: int) -> int:
        if i != u:
            return 0
        if u == 0:
            return 1
        return 1 + λ(i, u - 1)

    def Ϭ(o: List[int], s: int, acc: int) -> int:
        if s == 0:
            return acc
        return Ϭ(o, s - 1, acc + abs(o[s] - o[s - 1]))

    def ϱ(r: int, start: int, end: int) -> int:
        if start >= end:
            return r
        w = abs(start - end)
        return ϱ(r + w, start + 1, end)

    def Ω(Δ: int, Μ: int, Ν: int, П: int) -> int:
        if Μ >= Ν:
            return Δ
        Φ = Π = abs(arr[Μ] - arr[П])
        Χ = Δ
        Ψ = П
        Κ = Ν
        ⚝ = Φ if Φ < Δ else Δ
        # The line Λ is ambiguous in pseudocode; mimicking comparison but no side effect.
        # In pseudocode, Λ seems to assign based on comparison, but variables Λ and Κ are undefined/out of scope.
        # To maintain correctness, this line doesn't alter any outer variable.
        _ = (sorted([arr[Μ], arr[П]]), Κ) if Φ < Δ else (Χ, None)
        return Ω(⚝, Μ, Ν + 1, П)

    def ⛨(array: List[int]) -> Optional[Tuple[int, int]]:
        ⚜ = array
        ↻ = {}
        ↺ = 0

        nonlocal arr

        ⨀: Optional[Tuple[int, int]] = None
        Π: Optional[int] = None
        Β = 0
        🜇 = len(array) - 1
        Ξ = 0
        ☉ = 0

        def FUNC1(Ξ⃝: int) -> None:
            if Ξ⃝ > 🜇:
                return

            def FUNC2(☉⃝: int) -> None:
                nonlocal Π, ⨀
                if ☉⃝ > 🜇:
                    return
                if ☉⃝ != Ξ⃝:
                    Φ = abs(array[Ξ⃝] - array[☉⃝])
                    if Π is None:
                        Π = Φ
                        ⨀ = (min(array[Ξ⃝], array[☉⃝]), max(array[Ξ⃝], array[☉⃝]))
                    elif Φ < Π:
                        Π = Φ
                        ⨀ = (min(array[Ξ⃝], array[☉⃝]), max(array[Ξ⃝], array[☉⃝]))
                FUNC2(☉⃝ + 1)

            FUNC2(0)
            FUNC1(Ξ⃝ + 1)

        FUNC1(0)
        return ⨀

    return ⛨(arr)