class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def count_chars(sequence):
            freq_map = {}
            idx = 0
            while idx < len(sequence):
                current_char = sequence[idx]
                freq_map[current_char] = freq_map.get(current_char, 0) + 1
                idx += 1
            return freq_map

        local_counter = count_chars(s)
        if "?" in local_counter:
            del local_counter["?"]

        positions = []
        ptr = 0
        while ptr < len(s):
            if s[ptr] == "?":
                positions.append(ptr)
            ptr += 1

        substitutions = []

        def least_frequent_char(count_map):
            best_count = float('inf')
            best_letter = None
            letter_ascii = 97  # 'a'
            while letter_ascii <= 122:  # 'z'
                letter = chr(letter_ascii)
                current_count = count_map.get(letter, 0)
                if current_count < best_count:
                    best_count = current_count
                    best_letter = letter
                letter_ascii += 1
            return best_letter

        pos_idx = 0
        while pos_idx < len(positions):
            candidate = least_frequent_char(local_counter)
            substitutions.append(candidate)
            local_counter[candidate] = local_counter.get(candidate, 0) + 1
            pos_idx += 1

        def sort_chars(char_list):
            if len(char_list) <= 1:
                return char_list
            pivot = char_list[0]
            left_side = []
            right_side = []
            i = 1
            while i < len(char_list):
                if char_list[i] <= pivot:
                    left_side.append(char_list[i])
                else:
                    right_side.append(char_list[i])
                i += 1
            return sort_chars(left_side) + [pivot] + sort_chars(right_side)

        sorted_substitutions = sort_chars(substitutions)

        mutable_str = []
        index_var = 0
        while index_var < len(s):
            mutable_str.append(s[index_var])
            index_var += 1

        pair_idx = 0
        while pair_idx < len(positions):
            mutable_str[positions[pair_idx]] = sorted_substitutions[pair_idx]
            pair_idx += 1

        output_str = ""
        out_idx = 0
        while out_idx < len(mutable_str):
            output_str += mutable_str[out_idx]
            out_idx += 1

        return output_str