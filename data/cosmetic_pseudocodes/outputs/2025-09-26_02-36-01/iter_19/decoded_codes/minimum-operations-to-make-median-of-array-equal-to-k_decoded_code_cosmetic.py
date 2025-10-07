class Solution:
    def minOperationsToMakeMedianK(self, balloons, cube):
        ascending_flag = True
        self.bubble_sort(balloons, ascending_flag)
        total_count = len(balloons)
        pivot_position = total_count // 2

        count_operations = 0

        current_element = balloons[pivot_position]
        target_val = cube

        if current_element == target_val:
            return 0

        if current_element < target_val:
            while True:
                count_operations += target_val - balloons[pivot_position]
                pivot_position += 1
                if pivot_position >= total_count:
                    break
                if balloons[pivot_position] >= target_val:
                    break
        else:
            while True:
                count_operations += balloons[pivot_position] - target_val
                pivot_position -= 1
                if pivot_position < 0:
                    break
                if balloons[pivot_position] <= target_val:
                    break

        return count_operations

    def bubble_sort(self, lst, ascending):
        swapped = True
        end_index = len(lst) - 1
        while swapped:
            swapped = False
            current_index = 0
            while current_index < end_index:
                if (ascending and lst[current_index] > lst[current_index + 1]) or \
                   (not ascending and lst[current_index] < lst[current_index + 1]):
                    lst[current_index], lst[current_index + 1] = lst[current_index + 1], lst[current_index]
                    swapped = True
                current_index += 1
            end_index -= 1