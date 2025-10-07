class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            maxLength = 0
            count = 1

            def recurse(position):
                nonlocal maxLength, count
                if position >= len(s):
                    if maxLength < count:
                        maxLength = count
                    return

                if s[position] == s[position - 1]:
                    count += 1
                else:
                    if maxLength < count:
                        maxLength = count
                    count = 1
                recurse(position + 1)

            if not s:
                return 0
            recurse(1)
            return max(maxLength, count)

        answer = len(s)
        limit = 1 << len(s)

        def bitCount(val):
            result = 0
            while val > 0:
                if val & 1:
                    result += 1
                val >>= 1
            return result

        iter_ = 0
        while iter_ < limit:
            if bitCount(iter_) > numOps:
                iter_ += 1
                continue

            modifiableList = list(s)
            bitIndex = 0
            while bitIndex < len(s):
                mask = 1 << bitIndex
                if iter_ & mask:
                    currentChar = modifiableList[bitIndex]
                    newChar = '1' if currentChar == '0' else '0'
                    modifiableList[bitIndex] = newChar
                bitIndex += 1

            lengthCandidate = longest_uniform_substring(modifiableList)
            if answer > lengthCandidate:
                answer = lengthCandidate
            iter_ += 1

        return answer