from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    resultSequences: List[str] = []
    activeSequence: List[str] = []
    depthTracker: int = 0

    for currentChar in string_of_parentheses:
        if currentChar == '(':
            depthTracker += 1
            activeSequence.append(currentChar)
        elif currentChar == ')':
            depthTracker -= 1
            activeSequence.append(currentChar)
            if depthTracker == 0:
                resultSequences.append("".join(activeSequence))
                activeSequence = []

    return resultSequences