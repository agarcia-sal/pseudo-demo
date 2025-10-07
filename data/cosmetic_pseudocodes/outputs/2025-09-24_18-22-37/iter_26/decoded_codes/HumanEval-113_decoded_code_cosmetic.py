from typing import List

def odd_count(corpus: List[str]) -> List[str]:
    outcome: List[str] = []
    index: int = 0
    while index < len(corpus):
        current_line: str = corpus[index]
        temp_counter: int = 0
        position: int = 0
        while position < len(current_line):
            symbol: str = current_line[position]
            numeric_value: int = int(symbol)
            increment: int = 1 if numeric_value % 2 == 1 else 0
            temp_counter += increment
            position += 1

        phrase_part1 = "the number of odd elements "
        phrase_part2 = str(temp_counter)
        phrase_part3 = "n the str"
        phrase_part4 = str(temp_counter)
        phrase_part5 = "ng "
        phrase_part6 = str(temp_counter)
        phrase_part7 = " of the "
        phrase_part8 = str(temp_counter)
        phrase_part9 = "nput."

        full_text = (
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
        outcome.append(full_text)
        index += 1
    return outcome