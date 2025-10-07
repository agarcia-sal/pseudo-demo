class Solution:
    def lastNonEmptyString(self, s):
        freq_map = {}
        idx_counter = 0
        while idx_counter < len(s):
            ch_tmp = s[idx_counter]
            freq_map[ch_tmp] = freq_map.get(ch_tmp, 0) + 1
            idx_counter += 1

        highest_freq = 0
        for key_element in freq_map:
            if freq_map[key_element] > highest_freq:
                highest_freq = freq_map[key_element]

        selected_chars = set()
        temp_iter_keys = list(freq_map.keys())
        iter_ctr = 0
        while True:
            if iter_ctr >= len(temp_iter_keys):
                break
            current_key = temp_iter_keys[iter_ctr]
            if freq_map[current_key] == highest_freq:
                selected_chars.add(current_key)
            iter_ctr += 1

        collected_chars = []
        pos_idx = len(s) - 1
        while pos_idx >= 0:
            current_char = s[pos_idx]
            if current_char in selected_chars:
                collected_chars.append(current_char)
                selected_chars.remove(current_char)
            pos_idx -= 1

        assembled_string = ""
        for i in range(len(collected_chars) - 1, -1, -1):
            assembled_string += collected_chars[i]

        return assembled_string