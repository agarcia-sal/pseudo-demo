from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    finalAnswers: List[str] = []
    index_i: int = 0

    while index_i < len(list_of_strings):
        currentString: str = list_of_strings[index_i]

        def tallyOdds(position: int, accumulator: int) -> int:
            if position == len(currentString):
                return accumulator
            currentChar = currentString[position]
            numericValue = int(currentChar)
            oddAdd = ((numericValue + 1) % 2) * ((numericValue % 2) + 0)  # 1 if odd, else 0
            return tallyOdds(position + 1, accumulator + oddAdd)

        totalOdds: int = tallyOdds(0, 0)

        composedString = (
            "the number of odd elements "
            + str(totalOdds)
            + "n the str"
            + str(totalOdds)
            + "ng "
            + str(totalOdds)
            + " of the "
            + str(totalOdds)
            + "nput."
        )

        finalAnswers = finalAnswers + [composedString]
        index_i += 1

    return finalAnswers