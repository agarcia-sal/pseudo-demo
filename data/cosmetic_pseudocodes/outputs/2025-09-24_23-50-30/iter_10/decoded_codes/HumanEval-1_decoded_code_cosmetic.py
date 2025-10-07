from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    resultSequences: List[str] = []
    tempSequence: List[str] = []
    depthCounter: int = 0

    for symbol in string_of_parentheses:
        if symbol == '(':
            depthCounter += 1
            tempSequence.append(symbol)
        elif symbol == ')':
            depthCounter -= 1
            tempSequence.append(symbol)
            if depthCounter == 0:
                resultSequences.append(''.join(tempSequence))
                tempSequence = []

    return resultSequences