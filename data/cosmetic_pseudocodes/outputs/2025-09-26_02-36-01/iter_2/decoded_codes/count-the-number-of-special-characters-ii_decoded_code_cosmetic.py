class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        initialPositions = {}
        finalPositions = {}
        idx = 0
        while idx < len(word):
            ch = word[idx]
            if ch not in initialPositions:
                initialPositions[ch] = idx
            finalPositions[ch] = idx
            idx += 1

        totalSpecial = 0
        lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        idx2 = 0
        while idx2 < len(lower):
            lowChar = lower[idx2]
            upChar = upper[idx2]
            if lowChar in finalPositions and upChar in initialPositions:
                if finalPositions[lowChar] < initialPositions[upChar]:
                    totalSpecial += 1
            idx2 += 1
        return totalSpecial