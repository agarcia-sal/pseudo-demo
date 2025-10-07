class Solution:
    def countOfPairs(self, nums):
        _X1 = 10**9 + 7
        _X2 = len(nums)
        _X3 = max(nums)

        # Initialize 3D list _X4 of dimensions [_X2][_X3+1][_X3+1] with zeros
        _X4 = [[[0] * (_X3 + 1) for _ in range(_X3 + 1)] for __ in range(_X2)]

        # Base case initialization for the first element in nums
        for _X10 in range(nums[0] + 1):
            _X11 = nums[0] - _X10
            _X4[0][_X10][_X11] = 1

        # Fill _X4 using dynamic programming approach
        for _X12 in range(1, _X2):
            for _X13 in range(nums[_X12] + 1):
                _X14 = nums[_X12] - _X13
                for _X15 in range(_X13 + 1):
                    for _X16 in range(_X14, _X3 + 1):
                        _X4[_X12][_X13][_X14] = (_X4[_X12][_X13][_X14] + _X4[_X12 - 1][_X15][_X16]) % _X1

        _X17 = 0
        # Sum of all pairs where indices sum to last element of nums
        for _X18 in range(_X3 + 1):
            for _X19 in range(_X3 + 1):
                if _X18 + _X19 == nums[-1]:
                    _X17 = (_X17 + _X4[_X2 - 1][_X18][_X19]) % _X1

        return _X17