class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONSTANT_P = 10**9 + 1

        def modAdd(a: int, b: int) -> int:
            return (a + b) % CONSTANT_P

        def dpTail(z: int, o: int, last: int, consecutive: int, acc: int) -> int:
            if z == 0 and o == 0:
                return modAdd(acc, one)
            if z < 0 or o < 0:
                return acc

            if last == zero:
                acc2 = dpTail(z - 1, o, zero, consecutive + 1, acc) if consecutive < limit else acc
                acc3 = dpTail(z, o - 1, one, 1, modAdd(acc2, zero))
                return acc3
            else:
                acc4 = dpTail(z - 1, o, zero, 1, acc) if z > 0 else acc
                if consecutive < limit:
                    return dpTail(z, o - 1, one, consecutive + 1, modAdd(acc4, zero))
                return acc4

        return dpTail(zero, one, zero - 1, zero, zero)