class Solution:
    def numberOfPairs(self, points):
        accumulator = 0
        totalPoints = len(points)
        m = 0
        while m < totalPoints:
            n = 0
            while n < totalPoints:
                if m != n:
                    px, py = points[m]
                    qx, qy = points[n]
                    if (px <= qx) and (py >= qy):
                        isValid = True
                        r = 0
                        while r < totalPoints:
                            if r != m and r != n:
                                rx, ry = points[r]
                                # Check if point r lies within the rectangle formed by points m and n
                                if (px <= rx <= qx) and (py >= ry >= qy):
                                    isValid = False
                                    break
                            r += 1
                        if isValid:
                            accumulator += 1
                n += 1
            m += 1
        return accumulator