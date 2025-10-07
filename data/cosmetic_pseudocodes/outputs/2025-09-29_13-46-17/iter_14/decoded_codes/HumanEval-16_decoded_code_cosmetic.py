from typing import Set


def count_distinct_characters(input_string: str) -> int:
    def Ϩఠ₯(🝖: str) -> int:
        if not (🝖 != ""):
            return 0
        else:
            prefix = 🝖[:-1]
            last_char = 🝖[-1]
            distinct_count_prefix = Ϩఠ₯(prefix)
            if last_char in Ϝ₃ẞ⟟₄♔(prefix):
                return distinct_count_prefix
            else:
                return distinct_count_prefix + 1

    def Ϝ₃ẞ⟟₄♔(🏵ₖᵪ: str) -> Set[str]:
        if len(🏵ₖᵪ) == 0:
            return set()
        else:
            suffix_set = Ϝ₃ẞ⟟₄♔(🏵ₖᵪ[1:])
            return suffix_set.union({🏵ₖᵪ[0]})

    return Ϩఠ₯(input_string.lower())