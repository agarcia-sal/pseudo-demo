class Solution:
    def compressedString(self, omega: str) -> str:
        def toStr(num: int) -> str:
            if num == 0:
                return "0"
            digits = []
            tempNum = num
            while tempNum > 0:
                digits.append(chr((tempNum % 10) + ord('0')))
                tempNum //= 10
            return ''.join(digits[::-1])

        def equalChars(strA: str, idxA: int, charB: str) -> bool:
            return strA[idxA] == charB

        accumulation = []
        idxCounter = 0
        length = len(omega)

        while True:
            if not (idxCounter < length):
                break

            currentChar = omega[idxCounter]
            repetitionCount = 0

            while True:
                if not (idxCounter < length and equalChars(omega, idxCounter, currentChar)):
                    break
                repetitionCount += 1
                idxCounter += 1
                if repetitionCount == 9:  # 8 + 1 per pseudocode
                    break

            accumulation.append(toStr(repetitionCount) + currentChar)

        finalOutput = ''.join(accumulation)
        return finalOutput