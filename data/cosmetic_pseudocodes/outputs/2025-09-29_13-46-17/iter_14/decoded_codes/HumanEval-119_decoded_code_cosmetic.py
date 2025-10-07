from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def tally(chars: str, idx: int, accumulator: int) -> int:
            if idx >= len(chars):
                return accumulator

            def delta(ch: str) -> int:
                return 1 if ch == '(' else -1

            new_accumulator = accumulator + delta(chars[idx])
            if new_accumulator < 0:
                return -1
            return tally(chars, idx + 1, new_accumulator)

        result = tally(string_to_verify, 0, 0)
        return result == 0

    xαΩ = list_of_two_strings[0] + list_of_two_strings[1]
    ƃλ∂ = list_of_two_strings[1] + list_of_two_strings[0]
    Ϟ≈β = check(xαΩ)
    Ꙅ₮ = check(ƃλ∂)
    return 'Yes' if Ϟ≈β or Ꙅ₮ else 'No'