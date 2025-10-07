from typing import List

def odd_count(sequence_of_texts: List[str]) -> List[str]:
    accumulator: List[str] = []

    def recursive_process(index: int) -> None:
        if index == len(sequence_of_texts):
            return
        current_text: str = sequence_of_texts[index]

        def nested_recursive(char_index: int) -> int:
            if char_index == len(current_text):
                return 0
            is_odd = (int(current_text[char_index]) % 2) == 1
            return (1 if is_odd else 0) + nested_recursive(char_index + 1)

        tally: int = nested_recursive(0)
        composition = (
            "the number of odd elements "
            + str(tally)
            + "n the str"
            + str(tally)
            + "ng "
            + str(tally)
            + " of the "
            + str(tally)
            + "nput."
        )
        accumulator.append(composition)
        recursive_process(index + 1)

    recursive_process(0)
    return accumulator