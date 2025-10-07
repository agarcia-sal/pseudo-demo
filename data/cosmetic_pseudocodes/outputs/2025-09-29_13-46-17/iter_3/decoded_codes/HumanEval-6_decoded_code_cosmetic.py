from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(groupString: str) -> int:
        def evaluateDepth(index: int, depth: int, maxDepth: int) -> int:
            if index == len(groupString):
                return maxDepth
            char = groupString[index]
            if char == '(':
                newDepth = depth + 1
                newMax = max(maxDepth, newDepth)
                return evaluateDepth(index + 1, newDepth, newMax)
            else:
                return evaluateDepth(index + 1, depth - 1, maxDepth)
        return evaluateDepth(0, 0, 0)

    def isNonEmpty(s: str) -> bool:
        return s != ""

    splitGroups = parentheses_string.split(" ")
    resultList: List[int] = []
    for groupElement in splitGroups:
        if isNonEmpty(groupElement):
            resultList.append(parse_paren_group(groupElement))
    return resultList