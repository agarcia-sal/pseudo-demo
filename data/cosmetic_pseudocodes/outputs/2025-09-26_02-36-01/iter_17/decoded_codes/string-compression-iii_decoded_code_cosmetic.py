class Solution:
    def compressedString(self, word: str) -> str:
        totalParts = []
        idx = 0
        n = len(word)
        while True:
            if idx >= n:
                break
            currentChar = word[idx]
            cnt = 0
            while True:
                if idx >= n:
                    break
                if word[idx] != currentChar:
                    break
                cnt += 1
                idx += 1
                if cnt == 9:
                    break
            totalParts.append(str(cnt) + currentChar)
        return "".join(totalParts)