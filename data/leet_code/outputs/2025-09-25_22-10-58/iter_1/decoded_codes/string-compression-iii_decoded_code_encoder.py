class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        n = len(word)
        while i < n:
            c = word[i]
            count = 0
            while i < n and word[i] == c:
                count += 1
                i += 1
                if count == 9:
                    break
            comp.append(str(count) + c)
        return ''.join(comp)