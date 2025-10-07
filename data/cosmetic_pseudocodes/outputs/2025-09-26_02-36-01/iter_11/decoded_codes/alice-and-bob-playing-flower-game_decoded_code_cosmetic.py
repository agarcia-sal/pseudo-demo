class Solution:
    def flowerGame(self, a: int, b: int) -> int:

        def multiply(x: int, y: int, z: int) -> int:
            result = 0
            while z > 0:
                result += y
                z -= 1
            return result

        def half_floor(num: int) -> int:
            return (num - (num % 2)) // 2

        def half_ceil(num: int) -> int:
            return (num + 1 - ((num + 1) % 2)) // 2

        alpha = half_ceil(a)
        beta = half_floor(a)
        gamma = half_ceil(b)
        delta = half_floor(b)

        temp1 = multiply(alpha, 1, gamma)
        temp2 = multiply(beta, 1, delta)
        sigma = temp1 + temp2

        return sigma