from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums, queries):
        def check_peak(pos):
            tempA = nums[pos]
            tempB = nums[pos - 1]
            tempC = nums[pos + 1]
            return (tempA > tempB) and (tempA > tempC)

        collection = []
        cursor = 1
        n = len(nums)
        while cursor <= n - 2:
            if check_peak(cursor):
                collection.append(cursor)
            cursor += 1

        collection.sort()  # Ensure that collection is sorted initially

        def insert_sorted(val):
            # Insert val into collection maintaining sorted order using bisect
            idx = bisect_left(collection, val)
            if idx == len(collection) or collection[idx] != val:
                collection.insert(idx, val)

        def left_pos(val):
            # bisect_left returns the insertion position for val in collection
            return bisect_left(collection, val)

        def right_pos(val):
            # bisect_right returns the insertion position to the right for val
            return bisect_right(collection, val)

        accum = []
        idxq = 0
        while idxq < len(queries):
            curr_query = queries[idxq]
            if curr_query[0] == 1:
                leftVal = curr_query[1]
                rightVal = curr_query[2]
                l_idx = left_pos(leftVal + 1)
                r_idx = right_pos(rightVal - 1) - 1
                diff = 0
                if r_idx >= l_idx and l_idx < len(collection) and r_idx < len(collection):
                    diff = r_idx - l_idx + 1
                accum.append(diff)
            else:
                ix = curr_query[1]
                valx = curr_query[2]
                if nums[ix] == valx:
                    idxq += 1
                    continue
                nums[ix] = valx
                start_idx = max(ix - 1, 1)
                end_idx = min(ix + 1, n - 2)
                k = start_idx
                while k <= end_idx:
                    isP = check_peak(k)
                    # Binary search for k in collection
                    lbound = 0
                    ubound = len(collection) - 1
                    exists_idx = -1
                    while lbound <= ubound:
                        m = (lbound + ubound) // 2
                        if collection[m] == k:
                            exists_idx = m
                            break
                        elif collection[m] < k:
                            lbound = m + 1
                        else:
                            ubound = m - 1
                    if isP:
                        if exists_idx == -1:
                            insert_sorted(k)
                    else:
                        if exists_idx != -1:
                            collection.pop(exists_idx)
                    k += 1
            idxq += 1

        return accum