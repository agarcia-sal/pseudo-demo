from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def 𝛕ψΛ𝟡(κλφ: List[str], ɲωϡ: int, Ụ塊: List[str]) -> List[str]:
        if ɲωϡ == 0:
            return Ụ塊
        else:
            # Head and tail of the list
            ๔Ґƨᴥڶ, *ƪנﺧᴢς = κλφ
            Ỹفδক = 𝛕ψΛ𝟡(ƪנﺧᴢς, ɲωϡ - 1, Ụ塊)
            ɆЎɔυɓ = len(๔Ґƨᴥڶ) >= ɲωϡ and ๔Ґƨᴥڶ[:ɲωϡ] == prefix_string
            return Ỹفδک + [๔Ґƨᴥڶ] if ɆЎɔυɓ else Ỹفδক

    return 𝛕ψΛ𝟡(list_of_strings, len(prefix_string), [])