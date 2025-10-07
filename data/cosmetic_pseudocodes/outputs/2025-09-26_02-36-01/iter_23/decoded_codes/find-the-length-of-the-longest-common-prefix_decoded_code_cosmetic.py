class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        # Helper function to generate set of all prefixes from array of integers
        def generatePrefixSet(inputArray: list[int]) -> set[str]:
            resultSet = set()

            def traverse(index3: int) -> None:
                if index3 >= len(inputArray):
                    return
                stringForm = str(inputArray[index3])
                # accumulate all prefixes of stringForm
                def accumulatePrefixes(pos: int) -> None:
                    if pos > len(stringForm):
                        return
                    resultSet.add(stringForm[:pos])
                    accumulatePrefixes(pos + 1)

                accumulatePrefixes(1)
                traverse(index3 + 1)

            traverse(0)
            return resultSet

        setOne = generatePrefixSet(arr1)
        setTwo = generatePrefixSet(arr2)

        maxLength = 0
        prefixIterator = iter(setOne)

        def iteratePrefixes() -> None:
            nonlocal maxLength
            try:
                candidatePrefix = next(prefixIterator)
            except StopIteration:
                return
            if candidatePrefix in setTwo:
                currentLen = len(candidatePrefix)
                if currentLen > maxLength:
                    maxLength = currentLen
            iteratePrefixes()

        iteratePrefixes()
        return maxLength