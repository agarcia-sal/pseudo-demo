class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def frequencyMap(string: str) -> dict:
            freq = {}
            idx = 0
            while idx < len(string):
                ch = string[idx]
                freq[ch] = freq.get(ch, 0) + 1
                idx += 1
            return freq

        counts = frequencyMap(s)
        if "?" in counts:
            del counts["?"]

        positions = []
        pos = 0
        while pos < len(s):
            if s[pos] == "?":
                positions.append(pos)
            pos += 1

        substitutes = []
        idx2 = 0
        while idx2 < len(positions):
            current_min_count = 999999999
            current_min_char = None
            letter_idx = 0
            while letter_idx < 26:
                candidate = chr(ord('a') + letter_idx)
                if (candidate in counts and counts[candidate] < current_min_count) or (candidate not in counts and 0 < current_min_count):
                    current_min_count = counts[candidate] if candidate in counts else 0
                    current_min_char = candidate
                letter_idx += 1
            substitutes.append(current_min_char)
            if current_min_char in counts:
                counts[current_min_char] += 1
            else:
                counts[current_min_char] = 1
            idx2 += 1

        # insertion sort substitutes lexicographically ascending
        i = 1
        while i < len(substitutes):
            key_char = substitutes[i]
            j = i - 1
            while j >= 0 and substitutes[j] > key_char:
                substitutes[j + 1] = substitutes[j]
                j -= 1
            substitutes[j + 1] = key_char
            i += 1

        chars = []
        si = 0
        while si < len(s):
            chars.append(s[si])
            si += 1

        pair_index = 0
        while pair_index < len(positions):
            replaced_pos = positions[pair_index]
            replaced_char = substitutes[pair_index]
            chars[replaced_pos] = replaced_char
            pair_index += 1

        result = ""
        ri = 0
        while ri < len(chars):
            result += chars[ri]
            ri += 1

        return result