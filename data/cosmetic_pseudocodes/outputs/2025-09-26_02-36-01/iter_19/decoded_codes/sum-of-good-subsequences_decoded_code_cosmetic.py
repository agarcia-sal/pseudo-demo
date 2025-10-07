from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        θ = 10**9 + 7
        Ζ = defaultdict(int)  # map f with default 0
        Μ = defaultdict(int)  # map g with default 0

        α = 0
        while α < len(nums):
            ϕ = nums[α]
            Μ[ϕ] = (Μ[ϕ] + 1) % θ
            Ζ[ϕ] = (Ζ[ϕ] + ϕ) % θ

            Ζ[ϕ] = (Ζ[ϕ] + Ζ[ϕ - 1] + Μ[ϕ - 1] * ϕ) % θ
            Μ[ϕ] = (Μ[ϕ] + Μ[ϕ - 1]) % θ

            ζ = Ζ[ϕ]
            η = Μ[ϕ]
            Ζ[ϕ] = (ζ + Ζ[ϕ + 1] + Μ[ϕ + 1] * ϕ) % θ
            Μ[ϕ] = (η + Μ[ϕ + 1]) % θ

            α += 1

        β = 0
        for ε in Ζ.values():
            β = (β + ε) % θ

        π = β % θ
        return π