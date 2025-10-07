from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def check_peak(pos: int) -> bool:
            # Check whether nums[pos] is a peak compared to neighbors
            left_neighbor = nums[pos - 1]
            current_val = nums[pos]
            right_neighbor = nums[pos + 1]
            return current_val > left_neighbor and current_val > right_neighbor

        peak_positions = []

        def build_peaks() -> None:
            # Identify all initial peak positions
            for idx in range(1, len(nums) - 1):
                if check_peak(idx):
                    peak_positions.append(idx)

        def position_left(val: int) -> int:
            # Find left boundary insertion index for val in peak_positions
            return bisect_left(peak_positions, val)

        def position_right(val: int) -> int:
            # Find right boundary insertion index for val in peak_positions
            return bisect_right(peak_positions, val)

        def add_peak(newpos: int) -> None:
            insert_at = position_left(newpos)
            # Insert newpos if not already present
            if insert_at == len(peak_positions) or peak_positions[insert_at] != newpos:
                peak_positions.insert(insert_at, newpos)

        def delete_peak(delpos: int) -> None:
            loc = position_left(delpos)
            if loc < len(peak_positions) and peak_positions[loc] == delpos:
                peak_positions.pop(loc)

        build_peaks()
        answers = []
        qindex = 0
        n = len(nums)

        while qindex < len(queries):
            qry = queries[qindex]
            op = qry[0]

            if op == 1:
                l_bound = qry[1]
                r_bound = qry[2]
                # Find peaks in the interval [l_bound, r_bound]
                left_pos = position_right(l_bound - 1)
                right_pos = position_left(r_bound + 1) - 1
                if right_pos < left_pos:
                    answers.append(0)
                else:
                    answers.append(right_pos - left_pos + 1)
            else:
                idx_to_update = qry[1]
                new_val = qry[2]

                if nums[idx_to_update] == new_val:
                    qindex += 1
                    continue

                nums[idx_to_update] = new_val

                start_idx = max(1, idx_to_update - 1)
                end_idx = min(n - 2, idx_to_update + 1)

                for i in range(start_idx, end_idx + 1):
                    if check_peak(i):
                        add_peak(i)
                    else:
                        delete_peak(i)
            qindex += 1

        return answers