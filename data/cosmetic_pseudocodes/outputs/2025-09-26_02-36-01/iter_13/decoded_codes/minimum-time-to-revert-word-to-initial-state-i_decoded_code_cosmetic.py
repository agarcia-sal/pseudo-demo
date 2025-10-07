class Solution:
    def minimumTimeToInitialState(self, k: int) -> int:
        word = self.word  # Assume self.word is set before calling this function
        p = 1
        q = len(word)

        def equalSegments(s1, start1, s2, start2, length):
            for r in range(length):
                if s1[start1 + r] != s2[start2 + r]:
                    return False
            return True

        def conditionMet(current):
            threshold = current * k
            if threshold >= q:
                return True
            else:
                return equalSegments(word, threshold, word, 0, q - threshold)

        while True:
            if conditionMet(p):
                return p
            p += 1