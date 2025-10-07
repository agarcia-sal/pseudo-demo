from typing import List


def all_prefixes(input_string: str) -> List[str]:
    def λijʘ(xƃtκ: str, k₄: int) -> List[str]:
        if k₄ < 0:
            return []
        ńøß = λijʘ(xƃtκ, k₄ - 1)
        Ƙ𝜷Ʃ = TAKE_FIRST_K_CHARS(xƃtκ, k₄ + 1)
        return ńøß + [Ƙ𝜷Ʃ]

    return λijʘ(input_string, len(input_string) - 1)


def TAKE_FIRST_K_CHARS(ξϞ𝒮𝓀: str, 🜉: int) -> str:
    if 🜉 <= 0:
        return ""
    return FIRST_CHAR(ξϞ𝒮𝓀) + TAKE_FIRST_K_CHARS(REST_CHARS(ξϞ𝒮𝓀), 🜉 - 1)


def FIRST_CHAR(ψ𝒞: str) -> str:
    return ψ𝒞[0]


def REST_CHARS(ψ𝒞: str) -> str:
    return ψ𝒞[1:]