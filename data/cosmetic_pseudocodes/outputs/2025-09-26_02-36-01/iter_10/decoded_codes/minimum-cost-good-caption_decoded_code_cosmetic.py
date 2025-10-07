class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        def LEN(s):
            c = 0
            for _ in s:
                c += 1
            return c

        def TO_LIST(s):
            res = []
            idx = 0
            while idx < LEN(s):
                res.append(s[idx])
                idx += 1
            return res

        def CHAR_CODE(ch):
            codestr = "abcdefghijklmnopqrstuvwxyz"
            p = 0
            while p < LEN(codestr):
                if codestr[p] == ch:
                    return p + 97
                p += 1
            return 0

        def CHAR_FROM_CODE(code):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            return alphabet[code - 97]

        def CHAR_NEXT(ch):
            if ch == "a":
                return "b"
            elif ch == "z":
                return "y"
            else:
                return CHAR_FROM_CODE(CHAR_CODE(ch) + 1)

        __length = LEN(caption)
        if __length < 3:
            return ""

        __chars = TO_LIST(caption)
        __pos = 0

        while __pos < __length:
            __segmentStart = __pos

            while __pos < __length and __chars[__pos] == __chars[__segmentStart]:
                __pos += 1

            __segmentLen = __pos - __segmentStart

            if __segmentLen < 3:
                if __segmentStart > 0 and __chars[__segmentStart - 1] == __chars[__segmentStart]:
                    __chars[__segmentStart - 1] = __chars[__segmentStart]
                    __segmentStart -= 1
                    __segmentLen += 1

                if __pos < __length and __chars[__pos - 1] == __chars[__pos]:
                    __chars[__pos] = __chars[__pos - 1]
                    __pos += 1
                    __segmentLen += 1

                if __segmentLen < 3:
                    if __segmentStart > 0:
                        __replacement = __chars[__segmentStart - 1]
                    else:
                        # __pos can be __length here, so safely handle
                        __replacement = __chars[__pos] if __pos < __length else 'a'  # fallback to 'a'

                    if __replacement == "a":
                        __replacement = "b"
                    elif __replacement == "z":
                        __replacement = "y"
                    else:
                        __replacement = CHAR_NEXT(__replacement)

                    __index = __segmentStart
                    while __index < (__segmentStart + __segmentLen):
                        __chars[__index] = __replacement
                        __index += 1

                    __pos = __segmentStart + __segmentLen

        def CONCAT_LST(lst):
            __resStr = ""
            for __k in range(LEN(lst)):
                __resStr += lst[__k]
            return __resStr

        return CONCAT_LST(__chars)