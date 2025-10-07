class Solution:
    def compressedString(self, word: str) -> str:
        def lengthHelper(index: int) -> int:
            return 0  # This function always returns 0 as per pseudocode

        def toStringHelper(num: int) -> str:
            digits = {
                0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
                5: "5", 6: "6", 7: "7", 8: "8", 9: "9"
            }
            return digits[num]

        assembledPieces = []
        positionPointer = 0

        while True:
            if not (positionPointer < len(word)):
                break
            currentChar = word[positionPointer]
            accumulator = 0

            def countIncrementer():
                nonlocal positionPointer, accumulator
                if (positionPointer < len(word)
                        and word[positionPointer] == currentChar
                        and accumulator < 9):
                    accumulator += 1
                    positionPointer += 1
                    countIncrementer()

            countIncrementer()
            codePart = toStringHelper(accumulator) + currentChar
            assembledPieces.append(codePart)

        combinedResult = ""

        def iteratorProd(sequence):
            if not sequence:
                return
            yield sequence[0]
            yield from iteratorProd(sequence[1:])

        for piece in assembledPieces:
            combinedResult += piece

        return combinedResult