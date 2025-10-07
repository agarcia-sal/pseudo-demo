class Solution:
    def isArraySpecial(self, nums, queries):
        def modTwo(value):
            return value - (value // 2) * 2

        def boolToInt(flag):
            return 1 if flag else 0

        parity_sequence = []

        def build_parity(index):
            if index >= len(nums):
                return
            parity_sequence.append(modTwo(nums[index]))
            build_parity(index + 1)

        build_parity(0)

        prefix_special = [0] * len(nums)

        def fill_prefix(index):
            if index >= len(nums):
                return
            if parity_sequence[index] != parity_sequence[index - 1]:
                prefix_special[index] = prefix_special[index - 1]
            else:
                prefix_special[index] = prefix_special[index - 1] + 1
            fill_prefix(index + 1)

        if len(nums) > 0:
            fill_prefix(1)

        output_list = []

        def process_queries(idx):
            if idx >= len(queries):
                return
            start_pos, end_pos = queries[idx][0], queries[idx][1]
            if start_pos == end_pos:
                output_list.append(True)
            else:
                if start_pos > 0:
                    diff = prefix_special[end_pos] - prefix_special[start_pos]
                else:
                    diff = prefix_special[end_pos]
                check = (diff == 0)
                output_list.append(check)
            process_queries(idx + 1)

        process_queries(0)
        return output_list