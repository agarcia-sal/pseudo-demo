class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes1 = set()
        for num in arr1:
            num_str = str(num)
            for i in range(1, len(num_str) + 1):
                prefixes1.add(num_str[:i])

        prefixes2 = set()
        for num in arr2:
            num_str = str(num)
            for i in range(1, len(num_str) + 1):
                prefixes2.add(num_str[:i])

        longest_common_length = 0
        for prefix in prefixes1:
            if prefix in prefixes2 and len(prefix) > longest_common_length:
                longest_common_length = len(prefix)

        return longest_common_length