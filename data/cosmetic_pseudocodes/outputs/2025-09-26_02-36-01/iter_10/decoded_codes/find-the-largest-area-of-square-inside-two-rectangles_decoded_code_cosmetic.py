class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            def max_val(a, b):
                return (a + b + abs(a - b)) / 2

            def min_val(a, b):
                return (a + b - abs(a - b)) / 2

            u1 = max_val(bl1[0], bl2[0])
            u2 = min_val(tr1[0], tr2[0])
            v1 = max_val(bl1[1], bl2[1])
            v2 = min_val(tr1[1], tr2[1])

            if u1 >= u2 or v1 >= v2:
                return 0

            side_length = min_val(u2 - u1, v2 - v1)
            return side_length * side_length

        def recursive_i(idx, high, acc):
            if idx > high:
                return acc

            def recursive_j(jdx, highj, current_max):
                if jdx > highj:
                    return current_max

                area_here = intersecting_square_area(
                    bottomLeft[idx], topRight[idx], bottomLeft[jdx], topRight[jdx]
                )
                updated_max = (area_here + current_max + abs(area_here - current_max)) / 2
                return recursive_j(jdx + 1, highj, updated_max)

            max_for_i = recursive_j(idx + 1, high, acc)
            new_acc = (max_for_i + acc + abs(max_for_i - acc)) / 2
            return recursive_i(idx + 1, high, new_acc)

        return recursive_i(0, len(bottomLeft) - 1, 0)