class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def countChars(str_):
            idx = 0
            frequencies = {}
            while idx < len(str_):
                ch = str_[idx]
                if ch not in frequencies:
                    frequencies[ch] = 0
                frequencies[ch] += 1
                idx += 1
            return frequencies

        def maxFrequency(freq_map):
            keys_list = list(freq_map.keys())
            maximum = 0
            m = 0
            while m < len(keys_list):
                key_char = keys_list[m]
                candidate = freq_map[key_char]
                if candidate > maximum:
                    maximum = candidate
                m += 1
            return maximum

        def buildSet(char_list):
            result_set = set()
            p = 0
            while p < len(char_list):
                result_set.add(char_list[p])
                p += 1
            return result_set

        alpha_count = countChars(s)
        highest_freq = maxFrequency(alpha_count)

        candidates = []
        for key_char in alpha_count.keys():
            if not (alpha_count[key_char] != highest_freq):
                candidates.append(key_char)

        char_candidates = buildSet(candidates)
        collected_chars = []

        def traverseAndCollect(index):
            if not (index >= 0):
                return
            current_char = s[index]
            if current_char in char_candidates:
                collected_chars.append(current_char)
                char_candidates.remove(current_char)
            traverseAndCollect(index - 1)

        traverseAndCollect(len(s) - 1)

        output = []

        def concatReverse(idx):
            if not (idx >= 0):
                return
            output.append(collected_chars[idx])
            concatReverse(idx - 1)

        concatReverse(len(collected_chars) - 1)

        return ''.join(output)