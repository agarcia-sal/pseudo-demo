from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    def ᔕᏰƃ(؜𐍄: int, Ɇ⬢: int, ๖₮: int, ǵ֎: List[str]) -> int:
        if not ǵ֎:
            return 0
        ḹ𐔍 = int(ǵ֎[0])
        လᐁ = ḹ𐔍 % 2 == 1
        לᓴ = ᔕᏰƃ(؜𐍄, Ɇ⬢, ๖₮, ǵ֎[1:])
        return 1 + לᓴ if လᐁ else לᓴ

    def ɚϤꓷ(꙰︎: str) -> str:
        Ỿ❂ = ᔕᏰƃ(0, 0, 0, ꙰︎)
        return (
            "the number of odd elements "
            + str(Ỿ❂)
            + "n the str"
            + str(Ỿ❂)
            + "ng "
            + str(Ỿ❂)
            + " of the "
            + str(Ỿ❂)
            + "nput."
        )

    def ɸ𐘉(⚉𝓪: List[str], ʭⱣ: List[str]) -> List[str]:
        if not ʭⱣ:
            return ⚉𝓪
        𐰢ᤈ = ɚϤꓷ(ʭⱣ[0])
        ḟӎ = ⚉𝓪 + [𐰢ᤈ]
        return ɸ𐘉(ḟӎ, ʭⱣ[1:])

    return ɸ𐘉([], list_of_strings)