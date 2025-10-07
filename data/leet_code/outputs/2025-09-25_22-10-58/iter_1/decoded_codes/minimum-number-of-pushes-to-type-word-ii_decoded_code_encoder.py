from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse=True)
        total_pushes = 0
        key_presses = 1
        keys_assigned = 0
        for count in sorted_freq:
            total_pushes += count * key_presses
            keys_assigned += 1
            if keys_assigned == 8:
                keys_assigned = 0
                key_presses += 1
        return total_pushes