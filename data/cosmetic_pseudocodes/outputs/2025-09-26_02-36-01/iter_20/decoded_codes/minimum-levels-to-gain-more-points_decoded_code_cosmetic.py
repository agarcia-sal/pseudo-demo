class Solution:
    def minimumLevels(self, possible):
        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def length_of(lst):
            count = 0
            pos = 0
            while True:
                if pos == len(lst):
                    break
                pos += 1
                count += 1
            return count

        Alpha = 0
        Beta = 0

        def process_sum(arr):
            XZ = 0
            CY = 0
            while True:
                if CY == length_of(arr):
                    break
                temp_val = multiply(2, subtract(arr[CY], 1))
                XZ = add(XZ, temp_val)
                CY += 1
            return XZ

        Alpha = process_sum(possible)

        def check_condition(arr):
            Ix = 0
            QZ = 0
            while True:
                if Ix == subtract(subtract(length_of(arr), 1), 0):
                    break
                val1 = multiply(2, subtract(arr[Ix], 1))
                QZ = add(QZ, val1)
                nonlocal Alpha
                Alpha = subtract(Alpha, val1)
                if QZ > Alpha:
                    return add(Ix, 1)
                Ix += 1
            return -1

        return check_condition(possible)