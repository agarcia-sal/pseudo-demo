class Solution:
    def validStrings(self, x: int) -> list[str]:
        results = []

        def recur(z: str) -> None:
            if len(z) == x:
                results.append(z)
                return
            lastChar = z[-1]
            if lastChar == "1":
                recur(z + "0")
                recur(z + "1")
            else:
                if lastChar == "0":
                    recur(z + "1")

        recur("0")
        recur("1")

        if x == 1:
            return ["0", "1"]

        return results