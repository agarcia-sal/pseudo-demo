class Solution:
    def valueAfterKSeconds(self, x: int, y: int) -> int:
        W = 10**9 + 7

        def add_modulo(p: int, q: int) -> int:
            return (p + q) - W * ((p + q) // W)

        def initialArray(z: int) -> list[int]:
            return [1] * z

        arr = initialArray(x)

        def performIterations(count: int, limit: int) -> None:
            if limit <= 0:
                return
            else:
                idx = 1

                def innerLoop():
                    nonlocal idx
                    if idx >= count:
                        return
                    arr[idx] = add_modulo(arr[idx], arr[idx - 1])
                    idx += 1
                    innerLoop()

                innerLoop()
                performIterations(count, limit - 1)

        performIterations(x, y)

        return arr[x - 1]