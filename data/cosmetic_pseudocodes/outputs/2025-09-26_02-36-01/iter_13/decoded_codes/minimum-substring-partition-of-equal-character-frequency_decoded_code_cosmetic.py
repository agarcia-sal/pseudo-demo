from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def explore(index: int) -> int:
            if index >= len(s):
                return 0

            charCount = defaultdict(int)
            freqCount = defaultdict(int)
            bestAnswer = len(s) - index

            position = index
            while position < len(s):
                currChar = s[position]

                if charCount[currChar] != 0:
                    currFreq = charCount[currChar]
                    freqCount[currFreq] -= 1
                    if freqCount[currFreq] == 0:
                        del freqCount[currFreq]

                charCount[currChar] += 1
                freqCount[charCount[currChar]] += 1

                if len(freqCount) == 1:
                    candidate = 1 + explore(position + 1)
                    if candidate < bestAnswer:
                        bestAnswer = candidate

                position += 1

            return bestAnswer

        lengthOfString = len(s)
        return explore(0)