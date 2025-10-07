class Solution:
    def getPermutationIndex(self, perm):
        α = 0
        β = len(perm)
        γ = 10**9 + 1

        δ = [1] * β
        ζ = 1
        while True:
            ζ += 1
            if ζ > β - 1:
                break
            δ[ζ] = δ[ζ - 1] * ζ

        η = []
        θ = 1
        while θ <= β:
            η.append(θ)
            θ += 1

        ι = 0
        κ = 0
        while True:
            if κ > β - 1:
                break
            λ = 0
            μ = 0
            while μ < len(η):
                if η[μ] == perm[κ]:
                    λ = μ
                    μ = len(η)
                else:
                    μ += 1

            ι += λ * δ[(β - 1) - κ]
            η.pop(λ)
            κ += 1

        ν = ι % γ
        return ν