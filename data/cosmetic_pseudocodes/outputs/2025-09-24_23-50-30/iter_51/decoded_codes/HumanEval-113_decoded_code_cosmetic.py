from typing import List

def odd_count(sequence_of_texts: List[str]) -> List[str]:
    result_container: List[str] = []

    index: int = 0
    while index < len(sequence_of_texts):
        current_text: str = sequence_of_texts[index]

        def count_odd_digits_recursive(pos: int, acc: int) -> int:
            if pos == len(current_text):
                return acc
            digit_value: int = int(current_text[pos])
            new_acc: int = acc + (digit_value & 1)
            return count_odd_digits_recursive(pos + 1, new_acc)

        tally: int = count_odd_digits_recursive(0, 0)
        # construct message as per original pseudocode concatenation
        message_pieces: List[str] = [
            "the number of odd elements ",
            str(tally),
            "n the str",
            str(tally),
            "ng ",
            str(tally),
            " of the ",
            str(tally),
            "nput."
        ]
        result_container.append("".join(message_pieces))

        index += 1

    return result_container