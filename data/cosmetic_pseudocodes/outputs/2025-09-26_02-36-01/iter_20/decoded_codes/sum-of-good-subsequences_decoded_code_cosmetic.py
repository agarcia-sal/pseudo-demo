from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        MOD = 10**10 + 7
        ω = defaultdict(int)
        ψ = defaultdict(int)

        def adjust_values(μ):
            # Update ω[μ] and ψ[μ] based on neighboring values, modulo MOD
            ω[μ] = (ω[μ] + ω[μ - 1] + (ψ[μ - 1] * μ)) % MOD
            ψ[μ] = (ψ[μ] + ψ[μ - 1]) % MOD
            ω[μ] = (ω[μ] + ω[μ + 1] + (ψ[μ + 1] * μ)) % MOD
            ψ[μ] = (ψ[μ] + ψ[μ + 1]) % MOD

        for ϗ in nums:
            ψ[ϗ] += 1
            ω[ϗ] += ϗ
            adjust_values(ϗ)

        α = 0
        for key in ω.keys():
            α += ω[key]

        return α % MOD