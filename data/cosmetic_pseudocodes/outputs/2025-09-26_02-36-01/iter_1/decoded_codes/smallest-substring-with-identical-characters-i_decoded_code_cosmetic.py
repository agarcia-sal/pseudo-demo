class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            max_length = 0
            count = 1
            for i in range(1, len(s_list)):
                if s_list[i] == s_list[i - 1]:
                    count += 1
                else:
                    if count > max_length:
                        max_length = count
                    count = 1
            return count if count > max_length else max_length

        n = len(s)
        result = n
        total_combinations = 1 << n  # 2^n

        for mask in range(total_combinations):
            if bin(mask).count('1') > numOps:
                continue
            modified_chars = list(s)
            for pos in range(n):
                if (mask & (1 << pos)) != 0:
                    modified_chars[pos] = '1' if modified_chars[pos] == '0' else '0'
            length_uniform = longest_uniform_substring(modified_chars)
            if length_uniform < result:
                result = length_uniform

        return result