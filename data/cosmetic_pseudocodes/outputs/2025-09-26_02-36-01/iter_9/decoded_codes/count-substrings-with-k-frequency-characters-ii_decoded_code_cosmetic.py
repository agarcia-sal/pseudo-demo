class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def containsCharReachingK(freqMap: dict, limit: int) -> bool:
            for char in freqMap:
                if freqMap[char] >= limit:
                    return True
            return False

        frequencyTable = {}
        totalCount = 0
        startIndex = 0

        def incrementFreq(map_: dict, key: str) -> None:
            if key in map_:
                map_[key] += 1
            else:
                map_[key] = 1

        def decrementFreq(map_: dict, key: str) -> None:
            if key in map_:
                map_[key] -= 1
                if map_[key] == 0:
                    del map_[key]

        # Using iteration instead of recursion for efficiency and to avoid recursion limit
        nonlocal_start = [0]  # use list to allow modification in inner scope
        nonlocal_totalCount = [0]

        def processIndex(current: int, finish: int) -> None:
            while current < finish:
                currentChar = s[current]
                incrementFreq(frequencyTable, currentChar)
                while containsCharReachingK(frequencyTable, k):
                    leftChar = s[nonlocal_start[0]]
                    decrementFreq(frequencyTable, leftChar)
                    nonlocal_start[0] += 1
                nonlocal_totalCount[0] += nonlocal_start[0]
                current += 1

        processIndex(0, len(s))
        return nonlocal_totalCount[0]