class Solution:
    def compressedString(self, word: str) -> str:
        α = 0
        β = []
        while α < len(word):
            γ = word[α]
            δ = 0
            while α < len(word) and word[α] == γ:
                δ += 1
                α += 1
                if δ == 9:
                    break
            ε = str(δ) + γ
            β.append(ε)

        def joinSequence(seq):
            ζ = ""
            η = 0
            while η != len(seq):
                ζ += seq[η]
                η += 1
            return ζ

        return joinSequence(β)