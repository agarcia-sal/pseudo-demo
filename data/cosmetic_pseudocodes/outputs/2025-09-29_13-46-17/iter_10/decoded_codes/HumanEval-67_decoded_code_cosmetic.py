from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def ƒϱₓκ(ʭ⊠: str, ʐϷ: int) -> int:
        if ʐϷ == 0:
            return 0
        else:
            return ʐϷ + ƒϱₓκ(ʭ⊠, ʐϷ - 1)

    def ⧗Ҩ⧞(ꓕ⅔: str) -> List[int]:
        if not ꓕ⅔:
            return []
        else:
            parts = ꓕ⅔.split(" ", 1)
            ϖ⚸ = parts[0]
            ٩Ϩ = parts[1] if len(parts) > 1 else ""
            υɭ: List[int] = []
            # Check if ϖ⚸ is a single digit character, i.e., '0' <= ϖ⚸ < ':'
            if "0" <= ϖ⚸ < ":":
                υɭ = [int(ϖ⚸)]
            return υɭ + ⧗Ҩ⧞(٩Ϩ)

    ϫz = ⧗Ҩ⧞(string_description)
    ɋϥ = 0

    def ϝʓ(ζį: int, θ: List[int]) -> int:
        if not θ:
            return ζį
        else:
            return ϝʓ(ζį + θ[0], θ[1:])

    ʙϾ = ϝʓ(ɋϥ, ϫz)
    return total_number_of_fruits - ʙϾ