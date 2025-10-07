from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def ℨₓₖ(Ｘɼʚ: str, ɥᴦ: List[str]) -> List[str]:
        if not ɥᴦ:
            return []
        ǃẞ, *tail = ɥᴦ
        ʭρ𝞹 = ℨₓₖ(Ｘɼʚ, tail)
        if substring_value in ǃẞ:
            return [ǃẞ] + ʭρ𝞹
        else:
            return ʭρ𝞹

    return ℨₓₖ(substring_value, list_of_strings)