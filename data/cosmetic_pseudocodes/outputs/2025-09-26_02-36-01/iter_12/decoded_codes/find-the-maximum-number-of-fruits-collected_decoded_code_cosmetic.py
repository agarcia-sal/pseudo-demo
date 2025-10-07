class Solution:
    def maxCollectedFruits(self, fruits):
        size = len(fruits)

        arrayA = [(1, 1), (2, 1), (0, 1)]
        arrayB = [(1, 0), (1, -1), (1, 1)]
        arrayC = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def recurse(aX, aY, bX, bY, cX, cY):
            def outOfBounds(px, py):
                return px < 0 or px >= size or py < 0 or py >= size

            if outOfBounds(aX, aY) or outOfBounds(bX, bY) or outOfBounds(cX, cY):
                return -999999999

            if aX == aY == bX == bY == cX == cY == size - 1:
                return fruits[size - 1][size - 1]

            key = (aX, aY, bX, bY, cX, cY)
            if key in cache:
                return cache[key]

            sumFruits = fruits[aX][aY]
            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                sumFruits = 0

            if bX == cX and bY == cY:
                sumFruits += fruits[bX][bY]
            else:
                sumFruits += fruits[bX][bY] + fruits[cX][cY]

            best = -999999999

            for dx1, dy1 in arrayA:
                for dx2, dy2 in arrayB:
                    for dx3, dy3 in arrayC:
                        val = recurse(aX + dx1, aY + dy1, bX + dx2, bY + dy2, cX + dx3, cY + dy3)
                        if val > best:
                            best = val

            cache[key] = sumFruits + best
            return sumFruits + best

        return recurse(0, 0, 0, size - 1, size - 1, 0)