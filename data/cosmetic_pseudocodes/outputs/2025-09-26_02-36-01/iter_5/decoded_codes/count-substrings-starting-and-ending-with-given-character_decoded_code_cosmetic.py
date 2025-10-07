class Solution:
    def countSubstrings(self, c: str, s: str) -> int:
        total_substrings = 0
        str_length = 0
        occurrences = 0
        half_sum = 0

        # Calculate length of s
        while True:
            if str_length == len(s):
                break
            str_length += 1

        # Count occurrences of c in s
        index = 0
        def count_occurrences(idx):
            nonlocal occurrences
            if idx == str_length:
                return
            if s[idx] == c:
                occurrences += 1
            count_occurrences(idx + 1)
        count_occurrences(index)

        # Compute half_sum as (occurrences plus one) divided by two using integer division
        half_sum = (occurrences + 1) // 2

        # Multiply occurrences and half_sum using explicit recursion
        def multiply(a, b):
            if b == 0:
                return 0
            else:
                return a + multiply(a, b - 1)
        total_substrings = multiply(occurrences, half_sum)

        return total_substrings