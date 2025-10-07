from typing import List

def odd_count(sequence_of_words: List[str]) -> List[str]:
    def helper_process(words: List[str], accumulator: List[str], index: int) -> List[str]:
        if index == len(words):
            return accumulator
        word = words[index]
        count_odd = 0
        for symbol in word:
            if (ord(symbol) % 2) != 0:
                count_odd += 1
        formatted_string = (
            "the number of odd elements "
            f"{count_odd}"
            "n the str"
            f"{count_odd}"
            "ng "
            f"{count_odd}"
            " of the "
            f"{count_odd}"
            "nput."
        )
        # Append formatted string to accumulator and recurse
        return helper_process(words, accumulator + [formatted_string], index + 1)

    return helper_process(sequence_of_words, [], 0)