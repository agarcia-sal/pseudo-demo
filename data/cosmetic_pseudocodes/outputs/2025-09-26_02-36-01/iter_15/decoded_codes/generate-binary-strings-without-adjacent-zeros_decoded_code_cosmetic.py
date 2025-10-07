class Solution:
    def validStrings(self, n):
        if n - 1 != 0:
            validStringsCollection = []

            def backtrack(currentString):
                if len(currentString) == n:
                    validStringsCollection.append(currentString)
                    return
                lastChar = currentString[-1]
                if lastChar == "1":
                    backtrack(currentString + "0")
                    backtrack(currentString + "1")
                else:  # lastChar == "0"
                    backtrack(currentString + "1")

            backtrack("0")
            backtrack("1")
            return validStringsCollection
        else:
            return ["0", "1"]