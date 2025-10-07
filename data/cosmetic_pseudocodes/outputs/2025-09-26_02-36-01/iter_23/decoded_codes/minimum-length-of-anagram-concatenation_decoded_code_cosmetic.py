class Solution:
    def minAnagramLength(self, s: str) -> int:
        def buildSetFromString(inputStr: str) -> set:
            def recursiveAdd(index: int, accSet: set) -> set:
                if index >= len(inputStr):
                    return accSet
                updatedSet = accSet
                if inputStr[index] not in updatedSet:
                    updatedSet = updatedSet | {inputStr[index]}
                return recursiveAdd(index + 1, updatedSet)
            return recursiveAdd(0, set())

        tempSet = buildSetFromString(s)
        return len(tempSet)