class Solution:
    def countOfPeaks(self, nums, queries):
        def is_peak(index):
            prev_element = nums[index - 1]
            curr_element = nums[index]
            next_element = nums[index + 1]
            return curr_element > prev_element and curr_element > next_element

        peak_positions = []
        pos = 1
        n = len(nums)
        while pos <= n - 2:
            if is_peak(pos):
                peak_positions.append(pos)
            pos += 1

        answers = []

        for qry in queries:
            type_op = qry[0]
            if type_op == 1:
                left_bound = qry[1]
                right_bound = qry[2]

                left_pos = 0
                right_pos = len(peak_positions) - 1

                # Find left_pos: first peak position > left_bound
                while left_pos < len(peak_positions) and peak_positions[left_pos] <= left_bound:
                    left_pos += 1

                # Find right_pos: last peak position < right_bound + 1
                while right_pos >= 0 and peak_positions[right_pos] >= right_bound + 1:
                    right_pos -= 1

                count_peaks = right_pos - left_pos + 1
                if count_peaks < 0:
                    count_peaks = 0
                answers.append(count_peaks)

            else:  # type_op != 1 means update operation
                idx = qry[1]
                new_val = qry[2]

                if nums[idx] == new_val:
                    continue

                nums[idx] = new_val

                start_i = idx - 1
                if start_i < 1:
                    start_i = 1
                end_i = idx + 1
                if end_i > n - 2:
                    end_i = n - 2

                check_idx = start_i
                while check_idx <= end_i:
                    current_peak_flag = is_peak(check_idx)

                    # Binary search to find check_idx in peak_positions
                    position_found = False
                    left_border = 0
                    right_border = len(peak_positions) - 1
                    while left_border <= right_border:
                        middle = (left_border + right_border) // 2
                        if peak_positions[middle] == check_idx:
                            position_found = True
                            break
                        elif peak_positions[middle] < check_idx:
                            left_border = middle + 1
                        else:
                            right_border = middle - 1

                    if current_peak_flag:
                        if not position_found:
                            peak_positions.insert(left_border, check_idx)
                    else:
                        if position_found:
                            peak_positions.pop(middle)

                    check_idx += 1

        return answers