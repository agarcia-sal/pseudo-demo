class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:

        def strOfNumber(n: int) -> str:
            if n < 10:
                return chr(n + 48)
            else:
                return strOfNumber(n // 10) + chr((n % 10) + 48)

        def substr(s: str, start: int, end: int) -> str:
            # 1-based indexing per pseudocode
            if start > end or start < 1 or end > len(s):
                return ""
            if start == end:
                return s[start - 1]
            else:
                return s[start - 1] + substr(s, start + 1, end)

        def contains(set_to_check: set, val: str) -> bool:
            return val in set_to_check

        def lengthOf(s: str) -> int:
            if s == "":
                return 0
            else:
                return 1 + lengthOf(s[1:])

        def addPrefixes(numbers: list, accumulator: set, idx: int) -> set:
            if idx > len(numbers):
                return accumulator
            else:
                num_str = strOfNumber(numbers[idx - 1])

                def addSubPrefixes(str_: str, pos: int, acc: set) -> set:
                    if pos > lengthOf(str_):
                        return acc
                    else:
                        new_acc = acc.union({substr(str_, 1, pos)})
                        return addSubPrefixes(str_, pos + 1, new_acc)

                updated = addSubPrefixes(num_str, 1, accumulator)
                return addPrefixes(numbers, updated, idx + 1)

        setA = set()
        prefixesA = addPrefixes(arr1, setA, 1)

        setB = set()
        prefixesB = addPrefixes(arr2, setB, 1)

        def maxLengthCommon(set1: set, set2: set, elems: list, pos: int, current_max: int) -> int:
            if pos > len(elems):
                return current_max
            cur = elems[pos - 1]
            if contains(set2, cur):
                len_cur = lengthOf(cur)
                if len_cur > current_max:
                    return maxLengthCommon(set1, set2, elems, pos + 1, len_cur)
                else:
                    return maxLengthCommon(set1, set2, elems, pos + 1, current_max)
            else:
                return maxLengthCommon(set1, set2, elems, pos + 1, current_max)

        def setToArray(s: set, acc: list) -> list:
            if not s:
                return acc
            else:
                elem = next(iter(s))
                rem = s - {elem}
                return setToArray(rem, acc + [elem])

        arrPrefixesA = setToArray(prefixesA, [])

        answer = maxLengthCommon(prefixesA, prefixesB, arrPrefixesA, 1, 0)

        return answer