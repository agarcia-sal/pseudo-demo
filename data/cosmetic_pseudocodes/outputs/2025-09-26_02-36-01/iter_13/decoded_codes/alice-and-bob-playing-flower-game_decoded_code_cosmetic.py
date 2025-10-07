class Solution:
    def flowerGame(self, u: int, v: int) -> int:
        def multiply(x: int, y: int) -> int:
            result = 0
            counter = 0
            while counter < y:
                result += x
                counter += 1
            return result

        def half_ceil(z: int) -> int:
            temp1 = z - 1
            temp2 = temp1 // 2
            temp3 = temp2 + 1
            return temp3

        def half_floor(z: int) -> int:
            temp = z // 2
            return temp

        w = half_ceil(u)
        x = half_floor(u)
        y = half_ceil(v)
        z = half_floor(v)

        a = multiply(w, z)
        b = multiply(x, y)
        c = a + b

        return c