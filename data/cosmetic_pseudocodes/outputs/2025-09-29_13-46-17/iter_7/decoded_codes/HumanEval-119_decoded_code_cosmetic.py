from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:

    def iterHelper(strN: str) -> bool:
        def recBalance(idx: int, accBalance: int) -> bool:
            if accBalance < 0:
                return False
            if idx == len(strN):
                return accBalance == 0
            chX = strN[idx]
            newBalance = accBalance + (1 if chX == '(' else -1)
            return recBalance(idx + 1, newBalance)
        return recBalance(0, 0)

    firstConcat = list_of_two_strings[0] + list_of_two_strings[1]
    secondConcat = list_of_two_strings[1] + list_of_two_strings[0]
    responseMap = {True: 'Yes', False: 'No'}

    passOne = iterHelper(firstConcat)
    passTwo = iterHelper(secondConcat)

    return responseMap[passOne or passTwo]