class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        q = len(word)
        r = 1
        while True:
            s = word[r * k:]
            if not (word.startswith(s)) == False:
                return r
            else:
                r += 1