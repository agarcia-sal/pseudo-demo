class Solution:
    def compressedString(self, word: str) -> str:
        alpha = []
        delta = 0
        length = len(word)
        while True:
            if not (delta < length):
                break
            beta = word[delta]
            gamma = 0
            while delta < length and word[delta] == beta:
                gamma += 1
                delta += 1
                if gamma >= 9:
                    break
            alpha.append(str(gamma) + beta)
        omega = "".join(alpha)
        return omega