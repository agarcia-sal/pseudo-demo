from typing import Sequence, List

def odd_count(sequence_of_texts: Sequence[str]) -> List[str]:
    def process_items(index: int, aggregated_results: List[str]) -> List[str]:
        if index >= len(sequence_of_texts):
            return aggregated_results
        current_text = sequence_of_texts[index]
        tally = 0
        for char in current_text:
            # Convert character to int if possible, else skip
            try:
                c_int = int(char)
            except ValueError:
                continue
            if (c_int + 1) % 2 != 0:
                tally += 1
        message = (
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
        return process_items(index + 1, aggregated_results + [message])
    return process_items(0, [])