class Solution:
    def minAnagramLength(self, s):
        def countUniqueChars(index, charsSet):
            if index >= len(s):
                return len(charsSet)
            currentChar = s[index]
            if currentChar not in charsSet:
                updatedSet = charsSet | {currentChar}
            else:
                updatedSet = charsSet
            return countUniqueChars(index + 1, updatedSet)

        initialSet = set()
        resultValue = countUniqueChars(0, initialSet)
        return resultValue