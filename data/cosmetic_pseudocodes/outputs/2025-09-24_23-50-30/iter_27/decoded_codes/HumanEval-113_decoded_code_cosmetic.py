from typing import List


def odd_count(sequence_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []
    idx_outer: int = 0
    while idx_outer < len(sequence_of_strings):
        item_outer: str = sequence_of_strings[idx_outer]
        idx_inner: int = 0
        tally_odd: int = 0
        while idx_inner < len(item_outer):
            single_char: str = item_outer[idx_inner]
            numerical_value: int = int(single_char)
            if numerical_value % 2 == 1:
                tally_odd += 1
            idx_inner += 1
        phrase_part1: str = "the number of odd elements "
        phrase_part2: str = str(tally_odd)
        phrase_part3: str = "n the str"
        phrase_part4: str = str(tally_odd)
        phrase_part5: str = "ng "
        phrase_part6: str = str(tally_odd)
        phrase_part7: str = " of the "
        phrase_part8: str = str(tally_odd)
        phrase_part9: str = "nput."
        full_phrase: str = (
            phrase_part1
            + phrase_part2
            + phrase_part3
            + phrase_part4
            + phrase_part5
            + phrase_part6
            + phrase_part7
            + phrase_part8
            + phrase_part9
        )
        accumulator.append(full_phrase)
        idx_outer += 1
    return accumulator