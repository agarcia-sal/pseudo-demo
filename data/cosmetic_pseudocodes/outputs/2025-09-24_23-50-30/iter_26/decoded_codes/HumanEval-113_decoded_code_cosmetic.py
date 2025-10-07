from typing import List

def odd_count(array_of_sequences: List[List[str]]) -> List[str]:
    def helper_add_count(seq: List[str], acc: int) -> int:
        if not seq:
            return acc
        head_char = seq[0]
        tail_seq = seq[1:]
        increment = 1 if (int(head_char) % 2 == 1) else 0
        return helper_add_count(tail_seq, acc + increment)

    def process_elements(elems: List[List[str]]) -> List[str]:
        if not elems:
            return []
        current_element = elems[0]
        remaining_elements = elems[1:]
        odd_total = helper_add_count(current_element, 0)
        composed_string = (
            "the number of odd elements "
            + str(odd_total)
            + "n the str"
            + str(odd_total)
            + "ng "
            + str(odd_total)
            + " of the "
            + str(odd_total)
            + "nput."
        )
        return [composed_string] + process_elements(remaining_elements)

    output_collection = process_elements(array_of_sequences)
    return output_collection