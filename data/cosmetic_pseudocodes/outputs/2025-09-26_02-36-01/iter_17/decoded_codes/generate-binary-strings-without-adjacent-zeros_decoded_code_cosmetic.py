class Solution:
    def validStrings(self, n: int) -> list[str]:
        def backtrack(tempStr: str) -> None:
            if len(tempStr) == n:
                resultCollection.append(tempStr)
                return

            lastChar = tempStr[-1]
            if lastChar == "1":
                backtrack(tempStr + "0")
                backtrack(tempStr + "1")
            elif lastChar == "0":
                backtrack(tempStr + "1")

        resultCollection = []
        backtrack("0")
        backtrack("1")
        return resultCollection