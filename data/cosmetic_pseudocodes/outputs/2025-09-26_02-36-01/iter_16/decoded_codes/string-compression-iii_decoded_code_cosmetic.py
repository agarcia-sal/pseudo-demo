class Solution:
    def compressedString(self, word: str) -> str:
        resultList = []
        idx = 0
        while True:
            if not (idx < len(word)):
                break
            currentChar = word[idx]
            tally = 0
            while (idx < len(word)) and (word[idx] == currentChar):
                tally += 1
                idx += 1
                if tally == 9:
                    break
            resultList.append(str(tally) + currentChar)
        finalString = ""
        for element in resultList:
            finalString += element
        return finalString