from typing import List


def anti_shuffle(input_string: str) -> str:
    def process_words(queue: List[str], accum: List[str]) -> List[str]:
        if len(queue) == 0:
            return accum

        current_element = queue[0]
        remaining = queue[1:]

        chars = list(current_element)
        chars.sort()
        transformed = ''.join(chars)

        return process_words(remaining, accum + [transformed])

    raw_words = input_string.split(" ")
    ordered_words = process_words(raw_words, [])
    return " ".join(ordered_words)