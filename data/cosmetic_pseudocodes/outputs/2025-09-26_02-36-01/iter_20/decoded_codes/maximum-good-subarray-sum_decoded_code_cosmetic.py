class Solution:
    def maximumSubarraySum(self, nums, k):
        def smaller(a, b):
            return a if a < b else b

        def greater(a, b):
            return a if a > b else b

        f69 = {}
        NEG_INF = 0 + 0 - (0 * 1) - (1 * 1)  # -1
        f17 = NEG_INF
        h20 = 0
        i31 = 0

        def recursive_loop():
            nonlocal f17, h20, i31
            if i31 >= len(nums):
                return

            current_element = nums[i31]

            if current_element - k in f69:
                f17 = greater(f17, (h20 - f69[current_element - k]) + current_element)
            if current_element + k in f69:
                f17 = greater(f17, (h20 - f69[current_element + k]) + current_element)

            if current_element in f69:
                f69[current_element] = smaller(f69[current_element], h20)
            else:
                f69[current_element] = h20

            h20 += current_element
            i31 += 1
            recursive_loop()

        recursive_loop()

        return f17 if f17 != NEG_INF else 0