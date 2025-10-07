class Solution:
    def betterCompression(self, compressed: str) -> str:
        def AddCount(dic, key, amt):
            dic[key] = dic.get(key, 0) + amt

        temp_sym = ""
        temp_num = 0
        counts = {}
        i = 0
        n = len(compressed)
        while i < n:
            ch = compressed[i]
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
                if temp_sym != "":
                    AddCount(counts, temp_sym, temp_num)
                temp_sym = ch
                temp_num = 0
            else:
                # Multiply by 10 and add digit to build the number
                temp_num = (temp_num * 10) + (ord(ch) - ord('0'))
            i += 1
        if temp_sym != "":
            AddCount(counts, temp_sym, temp_num)

        def AscChars(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[(len(lst) + 1) // 2]
            left, right, equal = [], [], []
            for item in lst:
                if item < pivot:
                    left.append(item)
                elif item > pivot:
                    right.append(item)
                else:
                    equal.append(item)
            return AscChars(left) + equal + AscChars(right)

        sorted_keys = AscChars(list(counts.keys()))

        parts = []
        def IntToString(num):
            if num < 10:
                return chr(num + 48)
            else:
                return IntToString(num // 10) + chr((num % 10) + 48)

        for key_char in sorted_keys:
            val = counts[key_char]
            num_str = "0" if val == 0 else IntToString(val)
            parts.append(key_char + num_str)

        result = ""
        idx = 0
        while True:
            if idx >= len(parts):
                break
            result += parts[idx]
            idx += 1

        return result