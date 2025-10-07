class Solution:
    def compressedString(self, word: str) -> str:
        index = 0
        segments = []
        while True:
            if not (index < len(word)):
                break
            currentChar = word[index]
            tally = 0
            while index < len(word) and word[index] == currentChar:
                tally += 1
                index += 1
                if tally >= 9:
                    break
            self.AppendSegment(segments, tally, currentChar)
        return self.CombineSegments(segments)

    def AppendSegment(self, listRef: list, number: int, character: str) -> None:
        stringForm = self.ConvertNumberToString(number)
        entry = stringForm + character
        listRef.append(entry)

    def ConvertNumberToString(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = []
        value = num
        while value != 0:
            digitChar = chr(48 + (value % 10))
            digits.insert(0, digitChar)
            value //= 10
        return self.JoinCharacters(digits)

    def CombineSegments(self, listRef: list) -> str:
        outputString = ""
        for item in listRef:
            outputString += item
        return outputString

    def CharacterFromCode(self, code: int) -> str:
        return chr(code)

    def JoinCharacters(self, charList: list) -> str:
        resultString = ""
        for ch in charList:
            resultString += ch
        return resultString