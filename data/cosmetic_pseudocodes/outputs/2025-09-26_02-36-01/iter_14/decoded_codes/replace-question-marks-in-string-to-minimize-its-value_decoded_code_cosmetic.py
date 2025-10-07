class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def accumulate_frequencies(seq, freq_map):
            for elem in seq:
                freq_map[elem] = freq_map.get(elem, 0) + 1

        freq_dict = dict()
        accumulate_frequencies(list(s), freq_dict)

        if '?' in freq_dict:
            del freq_dict['?']

        positions = []
        idx = 0
        while idx < len(s):
            if s[idx] == '?':
                positions.append(idx)
            idx += 1

        replacements = []
        pos_idx = 0
        while pos_idx < len(positions):
            current_min = float('inf')
            chosen_char = None
            for letter_code in range(97, 123):  # a-z
                char_candidate = chr(letter_code)
                freq_val = freq_dict.get(char_candidate, 0)
                if freq_val < current_min:
                    chosen_char = char_candidate
                    current_min = freq_val
            replacements.append(chosen_char)
            freq_dict[chosen_char] = freq_dict.get(chosen_char, 0) + 1
            pos_idx += 1

        sorted_replacements = []
        temp_repl = replacements.copy()
        inserted_count = 0
        while inserted_count < len(temp_repl):
            smallest = 'z'
            smallest_index = -1
            for i, ch in enumerate(temp_repl):
                if ch <= smallest:
                    smallest = ch
                    smallest_index = i
            sorted_replacements.append(smallest)
            temp_repl.pop(smallest_index)
            inserted_count += 1

        char_array = list(s)
        pos_ptr = 0
        while pos_ptr < len(positions):
            pos_val = positions[pos_ptr]
            char_array[pos_val] = sorted_replacements[pos_ptr]
            pos_ptr += 1

        output_string = ''
        out_idx = 0
        while out_idx < len(char_array):
            output_string += char_array[out_idx]
            out_idx += 1

        return output_string