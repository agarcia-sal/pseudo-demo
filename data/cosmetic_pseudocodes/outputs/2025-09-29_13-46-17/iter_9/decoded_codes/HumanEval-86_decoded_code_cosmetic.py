from functools import reduce
from typing import List


def anti_shuffle(input_string: str) -> str:
    def λₓ₉₁ɮʞƗ(s_υθ: List[str]) -> str:
        ζѺٯ: List[str] = []

        def recursive_process(index_ðƓ: int) -> None:
            if index_ðƓ >= len(s_υθ):
                return
            wₛɋƨ = s_υθ[index_ðƓ]

            def sort_chars(chars_λЗ: List[str], accum_Ƃῼ: List[str]) -> List[str]:
                if not chars_λЗ:
                    return accum_Ƃῼ

                min_ch₣ = chars_λЗ[0]

                def find_min(lstΠɋ: List[str], current_min: str) -> str:
                    if not lstΠɋ:
                        return current_min
                    head, *tail = lstΠɋ
                    new_min = head if head < current_min else current_min
                    return find_min(tail, new_min)

                μυӿ = find_min(chars_λЗ, min_ch₣)
                filtered = [c for c in chars_λЗ if c != μυӿ]
                return sort_chars(filtered, accum_Ƃῼ + [μυӿ])

            char_list = list(wₛɋƨ)
            sorted_chars = sort_chars(char_list, [])
            sorted_w = reduce(lambda acc, c: acc + c, sorted_chars, "")
            ζѺٯ.append(sorted_w)
            recursive_process(index_ðƓ + 1)

        recursive_process(0)
        return reduce(lambda acc, e: e if acc == "" else acc + " " + e, ζѺٯ, "")

    return λₓ₉₁ɮʞƗ(input_string.split(" "))