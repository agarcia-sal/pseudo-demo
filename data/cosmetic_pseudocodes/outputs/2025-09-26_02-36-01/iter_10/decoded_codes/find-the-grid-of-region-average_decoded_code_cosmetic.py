from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        p = len(image)
        q = len(image[0]) if p > 0 else 0

        buffer = [[0]*q for _ in range(p)]
        tracker = [[0]*q for _ in range(p)]

        neighbors = [(-1,0), (1,0), (0,-1), (0,1)]

        def check_region(a: int, b: int) -> bool:
            # Check 3x3 region starting at (a,b)
            # For each cell, compare absolute difference with neighbors; all must <= threshold
            for u in range(a, a+3):
                for v in range(b, b+3):
                    for dx, dy in neighbors:
                        nx = u + dx
                        ny = v + dy
                        # neighbors must be inside the 3x3 block boundaries to check difference
                        # since pseudocode bounds neighbors by a+3 and b+3
                        if 0 <= u < p and 0 <= v < q and 0 <= nx < p and 0 <= ny < q:
                            # Only compare if neighbor also in 3x3 block to bound checks like pseudocode
                            if a <= nx < a+3 and b <= ny < b+3:
                                diff_val = abs(image[u][v] - image[nx][ny])
                                if diff_val > threshold:
                                    return False
            return True

        def average_region(c: int, d: int) -> int:
            sum_acc = 0
            for r in range(c, c + 3):
                for s in range(d, d + 3):
                    sum_acc += image[r][s]
            avg_res = sum_acc // 9
            return avg_res

        def process_rows(idx_outer: int):
            if idx_outer >= p - 2:
                return

            def process_cols(idx_inner: int):
                if idx_inner >= q - 2:
                    return

                if check_region(idx_outer, idx_inner):
                    local_avg = average_region(idx_outer, idx_inner)
                    for oi in range(idx_outer, idx_outer + 3):
                        for oj in range(idx_inner, idx_inner + 3):
                            buffer[oi][oj] += local_avg
                            tracker[oi][oj] += 1

                process_cols(idx_inner + 1)

            process_cols(0)
            process_rows(idx_outer + 1)

        process_rows(0)

        def finalize_rows(x_with: int):
            if x_with >= p:
                return

            def finalize_cols(y_with: int):
                if y_with >= q:
                    return

                if tracker[x_with][y_with] > 0:
                    buffer[x_with][y_with] = buffer[x_with][y_with] // tracker[x_with][y_with]
                else:
                    buffer[x_with][y_with] = image[x_with][y_with]

                finalize_cols(y_with + 1)

            finalize_cols(0)
            finalize_rows(x_with + 1)

        finalize_rows(0)

        return buffer