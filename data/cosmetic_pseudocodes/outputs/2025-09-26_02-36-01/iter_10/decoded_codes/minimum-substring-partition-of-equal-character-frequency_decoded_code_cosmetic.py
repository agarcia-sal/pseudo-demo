class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        from collections import defaultdict

        def dfs(k: int) -> int:
            def mapGetOrZero(m, x):
                return m[x] if x in m else 0

            if k >= len(s):
                return 0

            alphaCount = defaultdict(int)
            freqCount = defaultdict(int)
            result = len(s) - k

            def incrMap(m, key):
                m[key] = mapGetOrZero(m, key) + 1

            def decrMap(m, key):
                currVal = mapGetOrZero(m, key)
                if currVal > 0:
                    m[key] = currVal - 1
                    if m[key] == 0:
                        del m[key]

            curIndex = k
            while curIndex < len(s):
                ch = s[curIndex]

                if ch in alphaCount and alphaCount[ch] > 0:
                    oldFreqVal = alphaCount[ch]
                    decrMap(freqCount, oldFreqVal)

                incrMap(alphaCount, ch)
                newFreqVal = alphaCount[ch]
                incrMap(freqCount, newFreqVal)

                if len(freqCount) == 1:
                    candidate = 1 + dfs(curIndex + 1)
                    if candidate < result:
                        result = candidate

                curIndex += 1

            return result

        return dfs(0)