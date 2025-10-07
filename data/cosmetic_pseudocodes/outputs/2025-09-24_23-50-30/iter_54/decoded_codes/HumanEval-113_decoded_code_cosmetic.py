from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator: List[str] = []

    def process(index: int) -> None:
        if index >= len(list_of_strings):
            return
        str_elem = list_of_strings[index]
        tally = sum(1 for ch in str_elem if int(ch) % 2 == 1)
        phrase = (
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
        accumulator.append(phrase)
        process(index + 1)

    process(0)
    return accumulator