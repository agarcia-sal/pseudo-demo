class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def longest_uniform_substring(s_list):
            topLen = 0
            chainLen = 1

            idx = 1
            while idx < len(s_list):
                if s_list[idx] == s_list[idx - 1]:
                    chainLen += 1
                else:
                    if topLen < chainLen:
                        topLen = chainLen
                    chainLen = 1
                idx += 1

            return topLen if topLen > chainLen else chainLen

        result = len(s)
        cap = 1 << len(s)

        iterVal = 0
        while iterVal < cap:
            bitsCount = 0
            tempVal = iterVal
            while tempVal > 0:
                bitsCount += tempVal & 1
                tempVal >>= 1

            if bitsCount > numOps:
                iterVal += 1
                continue

            mod_s = list(s)
            posVar = 0
            while posVar < len(s):
                if (iterVal & (1 << posVar)) != 0:
                    mod_s[posVar] = '1' if mod_s[posVar] == '0' else '0'
                posVar += 1

            trialLen = longest_uniform_substring(mod_s)
            if result > trialLen:
                result = trialLen

            iterVal += 1

        return result