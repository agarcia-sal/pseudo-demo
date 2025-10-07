from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        segments = [word[i:i+k] for i in range(0, n, k)]
        segment_count = Counter(segments)
        max_count = max(segment_count.values(), default=0)
        result = len(segments) - max_count
        return result