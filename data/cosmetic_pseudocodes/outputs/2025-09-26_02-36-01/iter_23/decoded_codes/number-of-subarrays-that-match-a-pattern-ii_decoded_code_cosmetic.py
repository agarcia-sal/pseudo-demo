class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def compare_values(a, b):
            if not (a >= b):
                return 1
            else:
                if a == b:
                    return 0
                else:
                    return -1

        size1 = len(pattern)
        len_nums = len(nums)
        tally = 0
        relations = []

        def buildRelations(idx, max_idx):
            if idx > max_idx:
                return
            relations.append(compare_values(nums[idx], nums[idx + 1]))
            buildRelations(idx + 1, max_idx)

        buildRelations(0, len_nums - 2)

        total_to_check = len_nums - size1 - 1

        def checkMatches(pos, limit):
            nonlocal tally
            if pos > limit:
                return
            slice_to_compare = []

            def buildSlice(i, end_idx):
                if i > end_idx:
                    return
                slice_to_compare.append(relations[i])
                buildSlice(i + 1, end_idx)

            buildSlice(pos, pos + size1 - 1)

            if slice_to_compare == pattern:
                tally += 1

            checkMatches(pos + 1, limit)

        if total_to_check >= 0:
            checkMatches(0, total_to_check)

        return tally