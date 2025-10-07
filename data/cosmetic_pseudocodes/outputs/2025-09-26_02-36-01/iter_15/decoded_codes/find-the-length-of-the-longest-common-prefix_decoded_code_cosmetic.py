class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        alpha = set()
        beta = set()

        for val_a in arr1:
            str_a = str(val_a)
            for idx_b in range(1, len(str_a) + 1):
                alpha.add(str_a[:idx_b])

        for val_c in arr2:
            str_c = str(val_c)
            for idx_d in range(1, len(str_c) + 1):
                beta.add(str_c[:idx_d])

        maxLen = 0
        for pfx in alpha:
            if pfx in beta and len(pfx) > maxLen:
                maxLen = len(pfx)

        return maxLen