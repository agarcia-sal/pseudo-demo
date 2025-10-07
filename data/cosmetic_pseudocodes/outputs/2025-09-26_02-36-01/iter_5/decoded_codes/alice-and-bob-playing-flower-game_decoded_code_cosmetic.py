class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        def halfCeil(x: int) -> int:
            return (x + 1) // 2

        def halfFloor(x: int) -> int:
            return x // 2

        alpha = halfCeil(n)
        beta = halfFloor(n)
        gamma = halfCeil(m)
        delta = halfFloor(m)

        part1 = alpha * delta
        part2 = beta * gamma

        temp_sum = part1
        accumulator = temp_sum + part2
        result_sum = accumulator

        output_value = result_sum
        return output_value