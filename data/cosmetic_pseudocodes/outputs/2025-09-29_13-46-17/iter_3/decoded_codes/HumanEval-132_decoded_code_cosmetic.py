from typing import List, Tuple


def is_nested(string: str) -> bool:
    def collectIndices(pos: int, openStack: List[int], closeStack: List[int]) -> Tuple[List[int], List[int]]:
        if pos == len(string):
            return openStack, closeStack
        currentChar = string[pos]
        if currentChar == '[':
            return collectIndices(pos + 1, openStack + [pos], closeStack)
        else:
            return collectIndices(pos + 1, openStack, closeStack + [pos])

    openBrackets, closeBrackets = collectIndices(0, [], [])
    reversedCloseBrackets = closeBrackets[::-1]

    tally = 0
    cursor = 0
    closeLen = len(reversedCloseBrackets)
    for openIdx in openBrackets:
        if cursor < closeLen and openIdx < reversedCloseBrackets[cursor]:
            tally += 1
            cursor += 1

    return tally >= 2