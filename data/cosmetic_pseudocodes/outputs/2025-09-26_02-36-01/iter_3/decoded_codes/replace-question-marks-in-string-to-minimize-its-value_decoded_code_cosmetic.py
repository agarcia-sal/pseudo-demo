from collections import Counter

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counts_map = Counter(s)
        if '?' in counts_map:
            del counts_map['?']

        positions_of_qm = []
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch == '?':
                positions_of_qm.append(idx)
            idx += 1

        replacements = []
        alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        for pos in positions_of_qm:
            least_count = float('inf')
            candidate_char = None
            alpha_idx = 0
            while alpha_idx < len(alphabet):
                letter = alphabet[alpha_idx]
                current_count = counts_map.get(letter, 0)
                if current_count < least_count:
                    candidate_char = letter
                    least_count = current_count
                alpha_idx += 1
            replacements.append(candidate_char)
            counts_map[candidate_char] = counts_map.get(candidate_char, 0) + 1

        replacements.sort()

        char_array = []
        pointer = 0
        while pointer < len(s):
            char_array.append(s[pointer])
            pointer += 1

        rep_index = 0
        for pos in positions_of_qm:
            char_array[pos] = replacements[rep_index]
            rep_index += 1

        result_string = ''
        idx = 0
        while idx < len(char_array):
            result_string += char_array[idx]
            idx += 1

        return result_string