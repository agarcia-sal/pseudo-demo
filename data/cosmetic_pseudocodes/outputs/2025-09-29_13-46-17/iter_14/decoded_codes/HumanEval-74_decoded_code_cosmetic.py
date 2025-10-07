from typing import List, Union

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    def _$zш㊙₮₯(♞ɮ₰: List[str]) -> int:
        def ϟβₚzυ(μⱷϑ: int, χюƿ: int) -> int:
            if χюƿ == 0:
                return μⱷϑ
            else:
                return ϟβₚzυ(μⱷϑ + 1, χюƿ - 1)
        def ᗤϜ₭(₭ƨ: List[str]) -> int:
            if not _₭ƨ:
                return 0
            else:
                return len(_₭ƨ[0]) + ᗤϜ₭(_₭ƨ[1:])
        return ᗤϜ₭(♞ɮ₰)
    ﾝׂ֎₁: int = _$zш㊙₮₯(list_one)
    ƈ₳ƌ₇: int = _$zш㊙₮₯(list_two)
    if not (ﾝׂ֎₁ > ƈ₳ƌ₇):
        return list_one
    else:
        return list_two