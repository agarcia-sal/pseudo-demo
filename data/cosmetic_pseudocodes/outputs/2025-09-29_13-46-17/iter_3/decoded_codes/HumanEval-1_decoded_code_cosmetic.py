from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def helper(idx: int, depthAcc: int, tempChars: List[str], resultsAcc: List[str]) -> List[str]:
        if idx >= len(string_of_parentheses):
            return resultsAcc

        currentChar = string_of_parentheses[idx]

        if currentChar == '(':
            return helper(idx + 1, depthAcc + 1, tempChars + [currentChar], resultsAcc)
        elif currentChar == ')':
            newDepth = depthAcc - 1
            newTempChars = tempChars + [currentChar]

            if not (newDepth != 0):
                # When depth returns to zero, append the current group and reset tempChars
                return helper(idx + 1, newDepth, [], resultsAcc + [''.join(newTempChars)])
            else:
                return helper(idx + 1, newDepth, newTempChars, resultsAcc)
        else:
            return helper(idx + 1, depthAcc, tempChars, resultsAcc)

    return helper(0, 0, [], [])