class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        segments = []
        i = 0
        while i < n:
            segment = word[i:i + k]  # efficiently slice instead of concatenation loop
            segments.append(segment)
            i += k
        freq = {}
        for seg in segments:
            freq[seg] = freq.get(seg, 0) + 1
        max_freq = max(freq.values()) if freq else 0
        return len(segments) - max_freq