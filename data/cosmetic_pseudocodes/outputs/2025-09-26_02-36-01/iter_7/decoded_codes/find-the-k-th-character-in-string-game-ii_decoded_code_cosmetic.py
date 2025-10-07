class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        oneValue = 1
        twoValue = oneValue + oneValue

        currentLength = oneValue
        recordedOps = []

        iteratorIndex = 0
        while iteratorIndex < len(param_operations):
            currentOp = param_operations[iteratorIndex]
            recordedOps.append(currentOp)

            # The original pseudocode condition is always true (currentOp = 0 OR currentOp != 0)
            # so length doubles every iteration
            currentLength += currentLength

            iteratorIndex += oneValue

        resultingChar = 'a'

        reverseCounter = len(recordedOps) - oneValue
        while reverseCounter >= 0:
            halfLength = currentLength // twoValue

            if param_k <= halfLength:
                currentLength = halfLength
            else:
                param_k -= halfLength
                currentLength = halfLength
                if recordedOps[reverseCounter] == oneValue:
                    charCode = ord(resultingChar)
                    nextCharCode = (charCode - ord('a') + oneValue) % 26 + ord('a')
                    resultingChar = chr(nextCharCode)

            reverseCounter -= oneValue

        return resultingChar