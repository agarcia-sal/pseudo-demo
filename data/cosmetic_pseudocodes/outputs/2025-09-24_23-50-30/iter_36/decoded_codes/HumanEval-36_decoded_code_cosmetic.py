from typing import List


def fizz_buzz(integer_n: int) -> int:
    def accumulate_divisible(pivot: int, accumulator: List[int]) -> List[int]:
        if pivot == 0:
            return accumulator
        candidate = pivot - 1
        if candidate % 11 == 0 or candidate % 13 == 0:
            return accumulate_divisible(candidate, accumulator + [candidate])
        return accumulate_divisible(candidate, accumulator)

    collected_numbers = accumulate_divisible(integer_n, [])

    def concat_elements(elements: List[int]) -> str:
        if not elements:
            return ""
        return str(elements[0]) + concat_elements(elements[1:])

    combined_text = concat_elements(collected_numbers)

    def count_char(target: str, text: str, index: int, tot: int) -> int:
        if index == len(text):
            return tot
        increment = 1 if text[index] == target else 0
        return count_char(target, text, index + 1, tot + increment)

    return count_char('7', combined_text, 0, 0)