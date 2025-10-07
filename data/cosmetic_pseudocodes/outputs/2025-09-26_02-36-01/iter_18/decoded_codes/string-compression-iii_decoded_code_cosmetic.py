class Solution:
    def compressedString(self, word: str) -> str:
        assembled = []
        idx = 0
        n = len(word)
        while True:
            if not (idx < n):
                break
            symbol = word[idx]
            tally = 0
            continueLoop = True
            while continueLoop:
                if not (idx < n and word[idx] == symbol):
                    continueLoop = False
                else:
                    tally += 1
                    idx += 1
                    if tally == 9:
                        continueLoop = False
            assembled.append(str(tally) + symbol)
        finalString = ""
        for element in assembled:
            finalString += element
        return finalString