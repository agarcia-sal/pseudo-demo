from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def λH6❉(𓂀ζI: List[str]) -> List[str]:
        def Ƭ₁₃ᗢ(₮₥₳: str, ﻮᒷ: str) -> List[str]:
            if ﻮᒷ not in ₮₥₳:
                return []
            if not ₮₥₳:
                return []
            return [₮₥₳[0]] + Ƭ₁₃ᗢ(₮₥₳[1:], ﻮᒷ)

        def ꜱ҉₀₅(ɊɆ: List[str], Ɬ: str) -> List[str]:
            if not ɊɆ:
                return []
            if ɊɆ[0] in substring_value:
                return [ɊɆ[0]] + ꜱ҉₀₅(ɊɆ[1:], Ɬ)
            else:
                return ꜱ҉₀₅(ɊɆ[1:], Ɬ)

        return ꜱ҉₀₅(𓂀ζI, substring_value)

    return λH6❉(list_of_strings)