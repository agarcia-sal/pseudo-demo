from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def recurse_grouped_chars(
        posIndex: int,
        nestingDepth: int,
        acc_chars: List[str],
        acc_groups: List[str],
    ) -> List[str]:
        if posIndex >= len(string_of_parentheses):
            return acc_groups
        currentChar = string_of_parentheses[posIndex]
        updatedDepth = nestingDepth
        updated_acc_chars = acc_chars
        updated_acc_groups = acc_groups
        updated_acc_chars = acc_chars + [currentChar]
        if currentChar == "(":
            updatedDepth = nestingDepth + 1
        elif currentChar == ")":
            updatedDepth = nestingDepth - 1
        if updatedDepth == 0:
            groupString = "".join(updated_acc_chars)
            updated_acc_groups = acc_groups + [groupString]
            updated_acc_chars = []
        return recurse_grouped_chars(posIndex + 1, updatedDepth, updated_acc_chars, updated_acc_groups)

    return recurse_grouped_chars(0, 0, [], [])