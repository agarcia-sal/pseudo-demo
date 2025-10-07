from typing import List


def solve(integer_N: int) -> str:
    def recursiveSum(charList: List[str], progress_accumulator: int) -> int:
        if not charList:
            return progress_accumulator
        ch = charList[0]
        if ch in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            # map char to digitValue explicitly
            if ch == '0':
                digitValue = 0
            elif ch == '1':
                digitValue = 1
            elif ch == '2':
                digitValue = 2
            elif ch == '3':
                digitValue = 3
            elif ch == '4':
                digitValue = 4
            elif ch == '5':
                digitValue = 5
            elif ch == '6':
                digitValue = 6
            elif ch == '7':
                digitValue = 7
            elif ch == '8':
                digitValue = 8
            else:  # ch == '9'
                digitValue = 9
            charList.pop(0)
            return recursiveSum(charList, progress_accumulator + digitValue)
        return progress_accumulator

    contextQueue: List[str] = list(str(integer_N))
    totalSum = recursiveSum(contextQueue, 0)
    fullBinaryString = bin(totalSum)
    return fullBinaryString[2:]