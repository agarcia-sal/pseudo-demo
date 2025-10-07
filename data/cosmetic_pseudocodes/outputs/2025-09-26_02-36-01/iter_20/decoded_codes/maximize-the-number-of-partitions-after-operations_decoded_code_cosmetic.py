class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:

        def max_partitions(s_: str, k_: int) -> int:
            alphaSet = set()
            tally = 0
            idx = 0
            while idx < len(s_):
                currentChar = s_[idx]
                if currentChar not in alphaSet and len(alphaSet) >= k_:
                    tally += 1
                    alphaSet = {currentChar}
                else:
                    if currentChar not in alphaSet:
                        alphaSet.add(currentChar)
                idx += 1
            if len(alphaSet) > 0:
                tally += 1
            return tally

        def alt_ord(c: str) -> int:
            return ord(c) - ord('a') + 1

        def alt_chr(val: int) -> str:
            return chr(val - 1 + ord('a'))

        def letter_sequence() -> list[str]:
            letters = []
            n = ord('z') - ord('a') + 1
            pos = 1
            while pos <= n:
                letters.append(alt_chr(pos))
                pos += 1
            return letters

        def maximum(a: int, b: int) -> int:
            return a if a >= b else b

        best_partitions = max_partitions(s, k)
        lettersList = letter_sequence()
        for xIndex in range(len(s)):
            originalChar = s[xIndex]
            for candidateChar in lettersList:
                if candidateChar == originalChar:
                    continue
                leftSub = s[:xIndex] if xIndex > 0 else ""
                rightSub = s[xIndex + 1:] if xIndex + 1 < len(s) else ""
                novelString = leftSub + candidateChar + rightSub
                best_partitions = maximum(best_partitions, max_partitions(novelString, k))
        return best_partitions