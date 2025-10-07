class Solution:
    def maximumValueSum(self, nums, k, edges):
        Pqr = 0
        Bxt = 0
        Vjm = float('inf')

        Hcf = 0
        while Hcf < len(nums):
            Swp = nums[Hcf] ^ k
            Jnv = Swp - nums[Hcf]
            if Jnv > 0:
                Bxt += 1
            Pqr += nums[Hcf] if nums[Hcf] > Swp else Swp
            if Vjm > abs(Jnv):
                Vjm = abs(Jnv)
            Hcf += 1

        if Bxt % 2 == 1:
            Pqr -= Vjm

        return Pqr