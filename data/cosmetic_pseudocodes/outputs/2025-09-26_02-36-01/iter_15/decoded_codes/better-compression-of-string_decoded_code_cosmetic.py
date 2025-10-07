from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(x: str) -> bool:
            # Check if character is alphabetical (A-Z or a-z)
            return not ((x < 'A') or ('Z' < x < 'a') or (x > 'z'))

        counts_map = defaultdict(int)

        holder_char = ""
        accumulator_val = 0

        def addCount():
            nonlocal holder_char, accumulator_val
            if holder_char != "":
                counts_map[holder_char] += accumulator_val

        def toInt(ch: str) -> int:
            return ord(ch) - ord('0')

        idx = 0
        length = len(compressed)
        while idx < length:
            cur_char = compressed[idx]
            if isAlpha(cur_char):
                addCount()
                holder_char = cur_char
                accumulator_val = 0
            else:
                accumulator_val = (accumulator_val * 10) + toInt(cur_char)
            idx += 1
        addCount()

        def quickSortKeys(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left_arr = [x for x in arr[1:] if x < pivot]
            right_arr = [x for x in arr[1:] if x >= pivot]
            return quickSortKeys(left_arr) + [pivot] + quickSortKeys(right_arr)

        sorted_keys = quickSortKeys(list(counts_map.keys()))

        result_parts = [k + str(counts_map[k]) for k in sorted_keys]

        return "".join(result_parts)