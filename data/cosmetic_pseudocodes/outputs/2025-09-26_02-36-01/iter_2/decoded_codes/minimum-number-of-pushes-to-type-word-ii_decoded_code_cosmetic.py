class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = {}
        for ch in word:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        freq_values = sorted(freq_map.values(), reverse=True)

        total_cost = 0
        presses_needed = 1
        keys_used = 0

        for freq in freq_values:
            # contribution is freq * presses_needed
            total_cost += freq * presses_needed
            keys_used += 1

            if keys_used == 8:
                presses_needed += 1
                keys_used = 0

        return total_cost