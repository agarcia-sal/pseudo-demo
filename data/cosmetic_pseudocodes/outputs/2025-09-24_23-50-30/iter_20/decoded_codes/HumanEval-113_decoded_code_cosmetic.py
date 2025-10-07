from typing import List

def odd_count(strings: List[str]) -> List[str]:
    output: List[str] = []
    idx: int = 0
    while idx < len(strings):
        current_string: str = strings[idx]
        accumulator: int = 0
        pos: int = 0
        while pos < len(current_string):
            ch: str = current_string[pos]
            # Check if integer value of ch is odd
            if int(ch) % 2 != 0:
                accumulator += 1
            pos += 1
        message: str = (
            "the number of odd elements " + str(accumulator) +
            "n the str" + str(accumulator) + "ng " + str(accumulator) +
            " of the " + str(accumulator) + "nput."
        )
        output.append(message)
        idx += 1
    return output