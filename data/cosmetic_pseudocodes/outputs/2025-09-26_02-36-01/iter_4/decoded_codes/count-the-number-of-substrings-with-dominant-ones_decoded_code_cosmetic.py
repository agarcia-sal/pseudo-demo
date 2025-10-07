class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length_s = len(s)
        total_substrings = 0
        index_start = 0
        while index_start <= length_s - 1:
            count_ones = 0
            count_zeroes = 0
            index_end = index_start
            while index_end <= length_s - 1:
                current_char = s[index_end]
                if current_char == '1':
                    count_ones += 1
                else:
                    count_zeroes += 1
                threshold = count_zeroes * count_zeroes
                if count_ones >= threshold:
                    total_substrings += 1
                index_end += 1
            index_start += 1
        return total_substrings