class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        def helper_can_mark(stepCount):
            def init_neg_ones(length):
                return [-1] * length

            tally = 0
            limit = stepCount
            occur_arr = init_neg_ones(len(nums))
            ptr = 0
            while True:
                if ptr >= limit:
                    break
                pos = changeIndices[ptr] - 1
                occur_arr[pos] = ptr
                ptr += 1

            def total_of_list(inputList):
                acc = 0
                idx = 0
                while idx < len(inputList):
                    acc += inputList[idx]
                    idx += 1
                return acc

            required_decrements = total_of_list(nums)
            free_decrements = 0
            recorded_positions = set()

            def is_element_present(setCol, val):
                # Using 'in' would be idiomatic, but preserving function as per pseudocode
                for elt in setCol:
                    if elt == val:
                        return True
                return False

            iter_ = 0
            while iter_ < stepCount:
                current_pos = changeIndices[iter_] - 1

                if not is_element_present(recorded_positions, current_pos):
                    if occur_arr[current_pos] == iter_:
                        if nums[current_pos] <= free_decrements:
                            free_decrements -= nums[current_pos]
                            recorded_positions.add(current_pos)
                        else:
                            return False
                    else:
                        free_decrements += 1
                else:
                    free_decrements += 1

                iter_ += 1

            return len(recorded_positions) == len(nums)

        lbound = 0
        ubound = len(changeIndices) + 1
        while lbound < ubound:
            middle = (lbound + ubound) // 2
            if helper_can_mark(middle):
                ubound = middle
            else:
                lbound = lbound + 1

        if lbound <= len(changeIndices):
            return lbound
        else:
            return -1