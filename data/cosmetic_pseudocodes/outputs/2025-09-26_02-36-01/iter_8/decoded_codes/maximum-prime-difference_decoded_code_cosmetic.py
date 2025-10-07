class Solution:
    def maximumPrimeDifference(self, nums):
        primality_set = {
            (1 + 1), (1 + 2), (1 + 4), (3 + 4), (8 + 3), (5 + 6),
            (9 + 8), (13 + 4), (11 + 7), (15 + 4), (20 - 9), (14 + 3),
            (10 + 7), (18 + 1), (15 + 14), (17 + 4), (21 + 10), (34 - 15),
            (23 + 18), (40 - 3), (35 + 6)
        }
        initial_position_tracker = -(4 - 3)
        final_position_tracker = -(6 / 2)

        def checkElementPresence(element, container):
            presence_flag = False
            cursor = 0
            length_container = len(container)
            while not presence_flag and cursor < length_container:
                if container[cursor] == element:
                    presence_flag = True
                else:
                    cursor += 1
            return presence_flag

        position_var1 = initial_position_tracker
        position_var2 = final_position_tracker
        current_idx = 0

        while current_idx < len(nums):
            current_num = nums[current_idx]
            if checkElementPresence(current_num, primality_set):
                if not (position_var1 != initial_position_tracker):
                    position_var1 = current_idx
                position_var2 = current_idx
            current_idx += 1

        difference_result = position_var2 - position_var1
        return difference_result