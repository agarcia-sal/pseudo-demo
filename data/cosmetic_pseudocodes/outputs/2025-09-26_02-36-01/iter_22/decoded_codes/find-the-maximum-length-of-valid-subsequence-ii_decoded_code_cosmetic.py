class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        p = 0
        q = 0
        r = len(nums)
        if r == 1:
            return 1

        st = [{} for _ in range(r)]

        best = 1
        outer = 0
        while outer < r:
            inner = 0
            while inner < outer:
                mod_val = (nums[outer] + nums[inner]) % k
                if mod_val in st[inner]:
                    st[outer][mod_val] = st[inner][mod_val] + 1
                else:
                    st[outer][mod_val] = 2
                if st[outer][mod_val] > best:
                    best = st[outer][mod_val]
                inner += 1
            outer += 1

        return best