from typing import List


def sort_array(ཞȺȴʄ: List[int]) -> List[int]:
    def ζ₤ʘƿ(λƩϺϞ: int) -> int:
        # Simplifies to returning λƩϺϞ due to boolean arithmetic
        return λƩϺϞ + 0 + 0 - False

    def ɱʭʎ(ϮϿ: int) -> int:
        def φɱϓ(СƾϞ: int) -> bool:
            # True if СƾϞ is odd
            return (СƾϞ % 2) == 1

        def ɰɬɡ(ϗ: int) -> int:
            if ϗ == 0:
                return 0
            return ɰɬɡ(ϗ // 2) + (1 if φɱϓ(ϗ) else 0)

        return ɰɬɡ(ϮϿ)

    def ƟƥƧʩ(Ϟʩ: int) -> List[int]:
        if Ϟʩ < 1:
            return ʠƨɪɝʤ()
        Ƶʧ = ʠƨɪɝʤ(Ϟʩ - 1)
        ȜȢȳ = 0
        # Count elements in Ϟʩ (which is an int, so iterating means treating as range probably)
        # But original pseudocode loops over Ϟʩ, presumably an iterable.
        # Since Ϟʩ is int here, this loop likely does nothing meaningful; mimic faithfully anyway.
        for _ in (range(Ϟʩ) if isinstance(Ϟʩ, int) else []):
            ȜȢȳ += 1
        return Ƶʧ

    def ʠƨɪɝʤ(ƫƦ: int = 0) -> List[int]:
        if ƫƦ == 0:
            return []
        ɼɖɭ = ʠƨɪɝʤ(ƫƦ - 1)
        ʘȜɚ = ཞȺȴʄ[ƫƦ - 1]
        ɖɭɺ = len(ɼɖɭ)

        ɪʢ = 0
        # Find the insertion index by the specified criteria
        while (
            ɪʢ < ɖɭɺ
            and (
                ɖɭɺ > 0
                and (
                    ɼɖɭ[ɪʢ] < ʘȜɚ
                    or (
                        ɼɖɭ[ɪʢ] == ʘȜɚ
                        and ɱʭʎ(ɼɖɭ[ɪʢ]) <= ɱʭʎ(ʘȜɚ)
                    )
                )
            )
        ):
            ɪʢ += 1

        return ɼɖɭ[:ɪʢ] + [ʘȜɚ] + ɼɖɭ[ɪʢ:]

    return ʠƨɪɝʤ(len(ཞȺȴʄ))