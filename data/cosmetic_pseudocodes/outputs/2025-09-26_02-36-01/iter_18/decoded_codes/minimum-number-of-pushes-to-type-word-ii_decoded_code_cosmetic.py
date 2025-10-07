class Solution:
    def minimumPushes(self, word: str) -> int:
        alpha_counts = {}
        for ch in word:
            alpha_counts[ch] = alpha_counts.get(ch, 0) + 1

        freq_values = list(alpha_counts.values())

        freq_list = []
        while freq_values:
            max_index = 0
            for idx in range(1, len(freq_values)):
                if freq_values[idx] > freq_values[max_index]:
                    max_index = idx
            freq_list.append(freq_values[max_index])
            freq_values.pop(max_index)

        acc_pushes = 0
        press_count = 1
        key_count = 0
        pos = 0

        while pos < len(freq_list):
            acc_pushes += freq_list[pos] * press_count
            key_count += 1
            if key_count == 8:
                key_count = 0
                press_count += 1
            pos += 1

        return acc_pushes