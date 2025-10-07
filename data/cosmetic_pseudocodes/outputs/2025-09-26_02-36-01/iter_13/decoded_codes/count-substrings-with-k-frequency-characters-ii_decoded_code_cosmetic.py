class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def contains_char_meeting_threshold(dictParam, thresholdParam):
            for keyVar in dictParam:
                if dictParam[keyVar] >= thresholdParam:
                    return True
            return False

        accumulatorVar = 0
        mapVar = {}
        lowerBound = 0
        upperBound = 0  # although unused in recursion, kept for literal translation

        def increment_dict_entry(mappingParam, keyParam):
            mappingParam[keyParam] = mappingParam.get(keyParam, 0) + 1

        def decrement_dict_entry(mappingParam, keyParam):
            if keyParam in mappingParam:
                mappingParam[keyParam] -= 1
                if mappingParam[keyParam] == 0:
                    del mappingParam[keyParam]

        def recursive_loop(highIndexParam):
            nonlocal accumulatorVar, lowerBound
            if highIndexParam == len(s):
                return

            currentChar = s[highIndexParam]
            increment_dict_entry(mapVar, currentChar)

            while contains_char_meeting_threshold(mapVar, k):
                leftChar = s[lowerBound]
                decrement_dict_entry(mapVar, leftChar)
                lowerBound += 1

            accumulatorVar += lowerBound

            recursive_loop(highIndexParam + 1)

        recursive_loop(0)
        return accumulatorVar