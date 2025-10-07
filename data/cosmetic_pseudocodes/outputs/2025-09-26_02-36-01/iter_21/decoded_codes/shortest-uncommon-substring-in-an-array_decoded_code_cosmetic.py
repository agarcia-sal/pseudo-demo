from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        α = defaultdict(int)

        def ζ(ξ):
            return ξ == 0

        def λ():
            ρ = 0
            while True:
                if ρ >= len(arr):
                    break
                κ = arr[ρ]
                σ = len(κ)

                def μ(ο, π):
                    if ο >= π:
                        return
                    def ν(τ):
                        if τ >= π:
                            return
                        υ = κ[ο:τ]  # substring from ο to τ-1
                        α[υ] += 1
                        ν(τ + 1)
                    ν(ο + 1)
                    μ(ο + 1, π)

                μ(0, σ)
                ρ += 1
            # λ is a while loop, no recursion needed as in pseudocode

        λ()

        ξ = []
        α1 = len(arr) - 1
        β1 = 0
        while True:
            if β1 > α1:
                break
            γ = arr[β1]
            δ = len(γ)
            ε = ""

            def ι(ν, ο):
                if ν >= ο:
                    return
                def κ1(μ):
                    if μ >= ο:
                        return
                    ο1 = γ[ν:μ]  # substring ν to μ-1
                    λ1 = len(ο1)
                    if α[ο1] == 1:
                        nonlocal ε
                        if ε == "" or λ1 < len(ε) or (λ1 == len(ε) and ο1 < ε):
                            ε = ο1
                    κ1(μ + 1)
                κ1(ν + 1)
                ι(ν + 1, ο)

            ι(0, δ)
            ξ.append(ε)
            β1 += 1

        return ξ