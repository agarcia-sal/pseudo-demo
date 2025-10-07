class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        def collectPositions(text):
            mapLow = {}
            mapUp = {}
            for idx, ch in enumerate(text):
                if ch not in mapLow:
                    mapLow[ch] = idx
                mapUp[ch] = idx
            return mapLow, mapUp

        def alphabeticalPairs():
            lows = "abcdefghijklmnopqrstuvwxyz"
            ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            return list(zip(lows, ups))

        first, last = collectPositions(word)

        totalCount = 0
        pairs = alphabeticalPairs()
        for lowChar, upChar in pairs:
            if lowChar in last and upChar in first:
                if last[lowChar] < first[upChar]:
                    totalCount += 1
        return totalCount