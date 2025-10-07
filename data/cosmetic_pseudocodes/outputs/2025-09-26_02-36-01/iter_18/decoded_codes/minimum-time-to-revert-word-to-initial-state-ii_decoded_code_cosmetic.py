class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        xnyv = 1
        while True:
            ykdm = word[xnyv * k :]
            if word.startswith(ykdm):
                return xnyv
            xnyv += 1