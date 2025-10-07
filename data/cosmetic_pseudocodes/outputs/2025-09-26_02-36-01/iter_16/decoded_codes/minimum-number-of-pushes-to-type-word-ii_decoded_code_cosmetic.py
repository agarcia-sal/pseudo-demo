class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        counts = list(freq.values())
        counts.sort(reverse=True)

        total_pushes = 0
        multiplier = 1
        count_in_group = 0

        for cnt in counts:
            total_pushes += cnt * multiplier
            count_in_group += 1
            if count_in_group == 8:
                count_in_group = 0
                multiplier += 1

        return total_pushes