class Solution:
    def minEnd(self, n: int, q: int) -> int:
        def canConstruct(z: int) -> bool:
            alfa = q
            bravo = 1

            def recurse() -> bool:
                nonlocal alfa, bravo
                if alfa >= z:
                    return bravo == n
                alfa += 1
                if (alfa & q) == q:
                    bravo += 1
                    if bravo == n:
                        return True
                return recurse()

            return recurse()

        charlie = q
        delta = 200_000_000
        while charlie < delta:
            echo = (charlie + delta) // 2
            if canConstruct(echo):
                delta = echo
            else:
                charlie += 1
        return charlie