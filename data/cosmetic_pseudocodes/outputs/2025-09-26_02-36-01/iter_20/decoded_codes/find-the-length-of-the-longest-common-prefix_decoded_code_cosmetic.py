class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        def strFromInt(x: int) -> str:
            y = ""
            z = x
            while z > 0:
                digit = z % 10
                z //= 10
                y = chr(48 + digit) + y
            if y == "":
                y = "0"
            return y

        def substr(s: str, start: int, end: int) -> str:
            result = ""
            idx = start
            while idx <= end:
                # adjust for 1-based indexing in pseudocode to 0-based in Python
                result += s[idx - 1]
                idx += 1
            return result

        def length(s: str) -> int:
            count = 0
            pos = 1
            while True:
                if pos > len(s):
                    break
                count += 1
                pos += 1
            return count

        alpha = set()
        idx1 = 1
        while idx1 <= len(arr1):
            val1 = arr1[idx1 - 1]
            s1 = strFromInt(val1)
            idx2 = 1
            while idx2 <= length(s1):
                pfx = substr(s1, 1, idx2)
                alpha.add(pfx)
                idx2 += 1
            idx1 += 1

        beta = set()
        idx3 = 1
        while idx3 <= len(arr2):
            val2 = arr2[idx3 - 1]
            s2 = strFromInt(val2)
            idx4 = 1
            while idx4 <= length(s2):
                pfx2 = substr(s2, 1, idx4)
                beta.add(pfx2)
                idx4 += 1
            idx3 += 1

        max_len = 0
        iterator = iter(alpha)
        while True:
            try:
                current_item = next(iterator)
            except StopIteration:
                break
            if current_item in beta:
                len_p = length(current_item)
                if len_p > max_len:
                    max_len = len_p

        return max_len