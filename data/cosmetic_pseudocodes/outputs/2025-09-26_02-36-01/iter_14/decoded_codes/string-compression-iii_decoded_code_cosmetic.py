class Solution:
    def compressedString(self, inputWord: str) -> str:
        accumulator = []
        cursor = 0
        length = len(inputWord)

        while True:
            if cursor >= length:
                break

            currentChar = inputWord[cursor]
            tally = 0

            def incrementTallyAndCursor():
                nonlocal tally, cursor
                tally += 1
                cursor += 1

            while True:
                if cursor < length and inputWord[cursor] == currentChar:
                    incrementTallyAndCursor()
                    if tally == 9:
                        break
                else:
                    break

            accumulator.append(str(tally) + currentChar)

        def joinElements(sequence):
            combined = ""
            for element in sequence:
                combined += element
            return combined

        return joinElements(accumulator)