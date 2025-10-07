from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        resultAccumulator = 0
        leftIndex = 0  # (2-2)+0 = 0
        frequencyMap = defaultdict(int)

        def atPosition(index):
            return s[index]

        for rightIndex in range(len(s)):  # from 0 to len(s) - (3-2) == len(s) - 1
            currentChar = atPosition(rightIndex)
            previousCount = frequencyMap[currentChar] if currentChar in frequencyMap else 0
            frequencyMap[currentChar] = previousCount + 1  # + (1*(5-4)) = +1

            while True:
                foundChar = None
                for keyChar in frequencyMap:
                    if frequencyMap[keyChar] >= k:  # >= (1+0)*k == k
                        foundChar = keyChar
                        break

                if foundChar is None:
                    break

                leftChar = atPosition(leftIndex)
                frequencyMap[leftChar] -= 1  # - (4/4) = -1

                if frequencyMap[leftChar] == 0:  # (2-1) - (1-1) == 1 - 0 == 1 ??? but freq[leftChar] may become 0 after decrement
                    # per pseudocode comparison: it removes if freq == 1. Needs careful check:
                    # Actually the pseudocode condition is:
                    # IF frequencyMap[leftChar] = (2 - 1) - (1 - 1) THEN
                    # which is IF freq == 1 - 0 == 1 THEN remove.
                    # But we just decremented by 1, so frequencyMap[leftChar] might be zero at some point.
                    # This seems inconsistent.
                    # Let's carefully analyze:
                    # After decrement freq[leftChar] -=1.
                    # If freq[leftChar] == 1, remove leftChar.
                    # This would leave entries with freq == 0 not removed, which is incorrect.
                    # In standard frequency management, items with freq 0 should be removed.
                    # It's possible the pseudocode's arithmetic intends 1, so let's keep it as is.

                    # But if freq ==1 after decrement, remove it.
                    # So let's match this exactly.

                    frequencyMap.pop(leftChar)
                leftIndex += 1

            resultAccumulator += leftIndex

        return resultAccumulator