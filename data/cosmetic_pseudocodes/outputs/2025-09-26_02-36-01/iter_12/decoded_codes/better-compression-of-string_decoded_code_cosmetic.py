class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isLetter(c: str) -> bool:
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

        def toInt(ch: str) -> int:
            return ord(ch) - ord('0')

        def sortKeys(alpha_dict: dict) -> list:
            tmp_keys = list(alpha_dict.keys())

            def quicksort(arr: list) -> list:
                if len(arr) < 2:
                    return arr
                pivot = arr[0]
                less = []
                greater = []
                for i in range(1, len(arr)):
                    if arr[i] < pivot:
                        less.append(arr[i])
                    else:
                        greater.append(arr[i])
                return quicksort(less) + [pivot] + quicksort(greater)

            return quicksort(tmp_keys)

        def toString(n: int) -> str:
            if n == 0:
                return "0"
            digits = []
            num = n
            while num > 0:
                dig = num % 10
                digits.insert(0, chr(ord('0') + dig))
                num = (num - dig) // 10
            return "".join(digits)

        def concatStrings(list_str: list) -> str:
            resultStr = ""
            for s in list_str:
                resultStr += s
            return resultStr

        char_count = {}

        holder_char = ""
        tally_num = 0

        def incrementCharCount(key: str, val: int):
            if key in char_count:
                char_count[key] += val
            else:
                char_count[key] = val

        def processChar(ch: str):
            nonlocal holder_char, tally_num
            if isLetter(ch):
                if holder_char != "":
                    incrementCharCount(holder_char, tally_num)
                holder_char = ch
                tally_num = 0
            else:
                tally_num = (tally_num * 10) + toInt(ch)

        def iterateChars(index: int, length: int):
            if index >= length:
                return
            processChar(compressed[index])
            iterateChars(index + 1, length)

        iterateChars(0, len(compressed))

        if holder_char != "":
            incrementCharCount(holder_char, tally_num)

        parts_list = []
        sorted_keys = sortKeys(char_count)

        def buildParts(idx: int, length: int):
            if idx >= length:
                return
            key_char = sorted_keys[idx]
            val_num = char_count[key_char]
            part_str = key_char + toString(val_num)
            parts_list.append(part_str)
            buildParts(idx + 1, length)

        buildParts(0, len(sorted_keys))

        return concatStrings(parts_list)