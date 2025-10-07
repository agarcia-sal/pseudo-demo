class Solution:
    def maxSubstringLength(self, s: str) -> int:
        def tallyFrequencies(string: str) -> dict:
            freq_map = {}
            idx = 0
            n = len(string)
            while True:
                if idx >= n:
                    break
                ch = string[idx]
                if ch in freq_map:
                    freq_map[ch] += 1
                else:
                    freq_map[ch] = 1
                idx += 1
            return freq_map

        full_count = tallyFrequencies(s)
        z = -1
        len_s = len(s)

        alpha = 0
        while alpha < len_s:
            delta_map = {}
            beta = alpha
            while beta < len_s:
                curr_char = s[beta]
                if curr_char in delta_map:
                    delta_map[curr_char] += 1
                else:
                    delta_map[curr_char] = 1

                truth_flag = True
                keys_list = list(delta_map.keys())
                k_ind = 0
                while k_ind < len(keys_list):
                    key_c = keys_list[k_ind]
                    freq_in_delta = delta_map[key_c]
                    freq_in_full = full_count.get(key_c, 0)
                    if freq_in_delta < freq_in_full:
                        truth_flag = False
                        break
                    k_ind += 1

                keys_count_delta = len(keys_list)
                keys_count_full = len(full_count)

                if truth_flag and keys_count_delta < keys_count_full:
                    current_span_length = (beta - alpha) + 1
                    if current_span_length > z:
                        z = current_span_length

                beta += 1
            alpha += 1

        return z