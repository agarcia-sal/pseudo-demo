class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        o0 = len(word)
        o1 = 1
        while True:
            o2 = word[o1 * k : o0]
            if word.startswith(o2):
                return o1
            o1 += 1