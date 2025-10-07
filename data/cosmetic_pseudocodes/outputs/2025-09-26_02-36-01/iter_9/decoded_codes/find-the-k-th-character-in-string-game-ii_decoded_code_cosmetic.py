class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        def halveValue(val: int) -> int:
            return val // 2

        def incrementChar(c: str) -> str:
            next_code = ord(c) + 1
            if next_code > ord('z'):
                next_code = ord('a')
            return chr(next_code)

        currentLength = 1
        sequence = []
        idx = 0
        while idx < len(param_operations):
            sequence.append(param_operations[idx])
            currentLength *= 2
            idx += 1

        resultChar = 'a'
        pos = len(sequence) - 1
        while True:
            if pos < 0:
                break

            leftHalfLength = halveValue(currentLength)
            if param_k <= leftHalfLength:
                currentLength = leftHalfLength
            else:
                param_k -= leftHalfLength
                currentLength = leftHalfLength
                if sequence[pos] == 1:
                    resultChar = incrementChar(resultChar)
            pos -= 1

        return resultChar