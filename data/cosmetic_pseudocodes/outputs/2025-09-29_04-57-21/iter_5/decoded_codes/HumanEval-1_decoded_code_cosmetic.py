from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    resultAccumulator: List[str] = []
    tempBuffer: List[str] = []
    depthCounter: int = 0

    def recurse(index: int) -> None:
        nonlocal depthCounter
        if index == len(string_of_parentheses):
            return

        symbol = string_of_parentheses[index]

        if symbol == '(':
            depthCounter += 1
            tempBuffer.append(symbol)
        elif symbol == ')':
            depthCounter -= 1
            tempBuffer.append(symbol)

            if depthCounter == 0:
                resultAccumulator.append(''.join(tempBuffer))
                tempBuffer.clear()

        recurse(index + 1)

    recurse(0)
    return resultAccumulator