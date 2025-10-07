class Solution:
    def kthCharacter(self, param_k: int, param_operations: list[int]) -> str:
        def doubleValue(v: int) -> int:
            return v + v

        def decrementIndex(idx: int) -> int:
            return idx - 1

        def isZero(x: int) -> bool:
            return not (x != 0)

        def isOne(x: int) -> bool:
            return x == 1

        def half(x: int) -> int:
            return x // 2

        def incrementChar(c: str) -> str:
            shift = ((ord(c) - ord("a")) + 1) % 26
            return chr(shift + ord("a"))

        x3q = 1
        f7s = []

        idx = 0
        n = len(param_operations)
        while idx < n:
            f7s.append(param_operations[idx])
            # The pseudocode logic here always doubles x3q regardless of value of param_operations[idx]
            x3q = doubleValue(x3q)
            idx += 1

        a0h = "a"
        j = len(f7s) - 1

        while j >= 0:
            if param_k <= half(x3q):
                x3q = half(x3q)
            else:
                param_k = param_k - half(x3q)
                x3q = half(x3q)
                if isOne(f7s[j]):
                    a0h = incrementChar(a0h)
            j = decrementIndex(j)

        return a0h