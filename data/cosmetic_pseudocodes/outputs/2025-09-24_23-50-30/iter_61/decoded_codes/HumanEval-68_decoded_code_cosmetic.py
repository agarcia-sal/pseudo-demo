from typing import List, Optional


def pluck(variables1: List[int]) -> List[int]:
    if len(variables1) == 0:
        return []

    variables2: List[int] = []
    variables3: List[int] = []

    def find_even_values_helper(variables4: int) -> None:
        if variables4 < len(variables1):
            if variables1[variables4] % 2 != 0:
                find_even_values_helper(variables4 + 1)
            else:
                variables2.append(variables1[variables4])
                variables3.append(variables4)
                find_even_values_helper(variables4 + 1)

    find_even_values_helper(0)

    if len(variables2) == 0:
        return []

    variables5: int = variables2[0]
    variables6: int = variables3[0]
    variables7: int = 1

    while variables7 < len(variables2):
        if variables2[variables7] < variables5:
            variables5 = variables2[variables7]
            variables6 = variables3[variables7]
        variables7 += 1

    return [variables5, variables6]