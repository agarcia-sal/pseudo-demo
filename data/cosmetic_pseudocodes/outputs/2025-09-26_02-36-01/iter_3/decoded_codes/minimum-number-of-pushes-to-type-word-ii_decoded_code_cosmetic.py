class Solution:
    def minimumPushes(self, word: str) -> int:
        char_counts = {}
        idx = 0
        while idx < len(word):
            ch = word[idx]
            if ch in char_counts:
                char_counts[ch] += 1
            else:
                char_counts[ch] = 1
            idx += 1

        counts_list = []
        for key in char_counts:
            counts_list.append(char_counts[key])

        descending_counts = []
        while len(counts_list) > 0:
            max_val = counts_list[0]
            max_idx = 0
            pos = 1
            while pos < len(counts_list):
                if counts_list[pos] > max_val:
                    max_val = counts_list[pos]
                    max_idx = pos
                pos += 1
            descending_counts.append(max_val)
            counts_list.pop(max_idx)

        total_presses = 0
        current_key_press = 1
        pressed_keys_count = 0
        i = 0
        while i < len(descending_counts):
            frequency = descending_counts[i]
            product = 0
            multiplier = current_key_press
            # The repeated addition is equivalent to frequency * current_key_press
            while multiplier > 0:
                product += frequency
                multiplier -= 1
            total_presses += product
            pressed_keys_count += 1
            if pressed_keys_count == 8:  # 4 + 4 keys pressed
                pressed_keys_count = 0
                current_key_press += 1
            i += 1

        return total_presses