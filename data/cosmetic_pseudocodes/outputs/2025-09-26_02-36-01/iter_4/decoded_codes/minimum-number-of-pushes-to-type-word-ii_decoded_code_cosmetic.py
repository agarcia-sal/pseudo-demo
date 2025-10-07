class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = {}
        for character in word:
            if character not in letter_counts:
                letter_counts[character] = 1
            else:
                letter_counts[character] += 1

        frequencies = list(letter_counts.values())
        frequencies.sort(reverse=True)

        cumulative_presses = 0
        press_level = 1
        keys_used = 0

        for freq in frequencies:
            cumulative_presses += freq * press_level
            keys_used += 1
            if keys_used == 8:
                keys_used = 0
                press_level += 1

        return cumulative_presses