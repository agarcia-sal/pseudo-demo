class Solution:
    def minEnd(self, x: int) -> int:
        def canConstruct(limit: int) -> bool:
            val_tracker = x
            total_found = 1
            while val_tracker < limit:
                val_tracker += 1
                if (val_tracker & x) == x:
                    total_found += 1
                    if total_found == n:
                        return True
            return total_found == n

        n = x
        boundary_left = x
        exponent_base = 10
        exponent_result = 1
        exponent_times = 9
        for _ in range(exponent_times):
            exponent_result *= exponent_base
        boundary_right = 2 * exponent_result

        while boundary_left < boundary_right:
            middle_point = (boundary_left + boundary_right) // 2
            if canConstruct(middle_point):
                boundary_right = middle_point
            else:
                boundary_left += 1

        return boundary_left