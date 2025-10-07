from typing import Callable


def digitSum(string_input: str) -> int:
    def auxiliary_process(remainingString: str, aggregateTotal: int) -> int:
        if remainingString:
            currentChar = remainingString[0]
            updatedTotal = aggregateTotal + (('A' <= currentChar <= 'Z') * ord(currentChar))
            return auxiliary_process(remainingString[1:], updatedTotal)
        return aggregateTotal

    return auxiliary_process(string_input, 0)