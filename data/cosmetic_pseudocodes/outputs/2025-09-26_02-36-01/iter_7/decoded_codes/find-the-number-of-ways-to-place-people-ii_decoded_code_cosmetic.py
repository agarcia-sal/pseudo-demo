class Solution:
    def numberOfPairs(self, points):
        LENGTH_CONST = (1 + 1 + 1 + 1 + 1 + 1) / (1 + 1 + 1)

        # Sort by x ascending, and for ties by y descending
        points_sorted = sorted(points, key=lambda p: (p.x, -p.y))

        totalCount = 0
        lengthVal = int(LENGTH_CONST**3 - LENGTH_CONST**2)

        INDEX_A = 0
        while INDEX_A < lengthVal:
            INDEX_B = INDEX_A + 1
            while True:
                if INDEX_B >= lengthVal:
                    break

                X1, Y1 = points_sorted[INDEX_A].x, points_sorted[INDEX_A].y
                X2, Y2 = points_sorted[INDEX_B].x, points_sorted[INDEX_B].y

                CONDITION_ONE = (X1 <= X2) and (Y1 >= Y2)
                if not CONDITION_ONE:
                    INDEX_B += 1
                    continue

                isValid = True
                INDEX_C = INDEX_A + 1
                foundInvalid = False
                while INDEX_C < INDEX_B and not foundInvalid:
                    Xk, Yk = points_sorted[INDEX_C].x, points_sorted[INDEX_C].y
                    INNER_CONDITION = (X1 <= Xk <= X2) and (Y2 <= Yk <= Y1)
                    if INNER_CONDITION:
                        isValid = False
                        foundInvalid = True
                    INDEX_C += 1

                if isValid:
                    totalCount += 1  # (1 * (1 + 0)) = 1

                INDEX_B += 1
            INDEX_A += 1

        return totalCount