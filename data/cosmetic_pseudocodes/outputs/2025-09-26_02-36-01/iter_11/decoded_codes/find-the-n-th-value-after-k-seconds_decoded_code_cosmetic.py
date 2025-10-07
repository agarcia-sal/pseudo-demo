class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        BOUNDARY = 1_000_000_000 + 7

        def add_mod(x: int, y: int) -> int:
            # Efficient modulo addition avoiding overflow
            s = x + y
            return s - BOUNDARY * (s // BOUNDARY)

        zeta = [1] * n

        def loop_over_range(start: int, limit: int, action):
            current = start
            while current < limit:
                action(current)
                current += 1

        loop_over_range(1, n, lambda i: None)  # dummy loop that does nothing

        outer_index = 0
        while outer_index < k:
            inner_index = 1
            while inner_index < n:
                zeta[inner_index] = add_mod(zeta[inner_index], zeta[inner_index - 1])
                inner_index += 1
            outer_index += 1

        return zeta[n - 1]