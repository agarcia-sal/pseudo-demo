from typing import List

def strange_sort_list(nums: List[int]) -> List[int]:
    output: List[int] = []
    toggle: bool = True
    while len(nums) > 0:
        if toggle:
            smallest = nums[0]
            for element in nums:
                if element < smallest:
                    smallest = element
            output.append(smallest)
            removal_index = 0
            for i in range(len(nums)):
                if nums[i] == smallest:
                    removal_index = i
                    break
            nums.pop(removal_index)
        else:
            largest = nums[0]
            for element in nums:
                if element > largest:
                    largest = element
            output.append(largest)
            removal_index = 0
            for i in range(len(nums)):
                if nums[i] == largest:
                    removal_index = i
                    break
            nums.pop(removal_index)
        toggle = not toggle
    return output