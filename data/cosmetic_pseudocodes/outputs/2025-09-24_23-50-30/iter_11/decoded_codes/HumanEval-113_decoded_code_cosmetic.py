from typing import List

def odd_count(array_of_texts: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx: int = 0
    while idx < len(array_of_texts):
        current_text: str = array_of_texts[idx]
        tally: int = 0
        for ch in current_text:
            if int(ch) % 2 != 0:
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
        output_collection.append(message)
        idx += 1
    return output_collection