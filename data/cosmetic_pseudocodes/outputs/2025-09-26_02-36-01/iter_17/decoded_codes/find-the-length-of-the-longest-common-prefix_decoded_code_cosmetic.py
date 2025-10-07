class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        setA = set()
        setB = set()

        def fillSet(collection: list[int], outputSet: set[str]) -> None:
            for val_num in collection:
                val = str(val_num)
                idx_inner = 1
                while idx_inner <= len(val):
                    part = val[:idx_inner]
                    outputSet.add(part)
                    idx_inner += 1

        fillSet(arr1, setA)
        fillSet(arr2, setB)

        max_len = 0
        for currPrefix in setA:
            if currPrefix in setB and len(currPrefix) > max_len:
                max_len = len(currPrefix)

        return max_len