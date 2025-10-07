class Solution:
    def flowerGame(self, gamma, delta):
        alpha = (gamma + 1) / 2
        beta = gamma / 2

        sigma = (delta + 1) / 2
        tau = delta / 2

        epsilon = (beta * sigma) + (alpha * tau)

        return epsilon