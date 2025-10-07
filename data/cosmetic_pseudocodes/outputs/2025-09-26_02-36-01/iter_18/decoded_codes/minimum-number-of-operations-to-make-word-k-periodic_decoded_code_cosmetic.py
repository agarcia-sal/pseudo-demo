class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        substrings = []
        i = 0
        while i <= n - 1:
            substrings.append(word[i:i+k])
            i += k

        frequency = {}
        for sub in substrings:
            frequency[sub] = frequency.get(sub, 0) + 1

        max_freq = max(frequency.values(), default=0)
        return len(substrings) - max_freq