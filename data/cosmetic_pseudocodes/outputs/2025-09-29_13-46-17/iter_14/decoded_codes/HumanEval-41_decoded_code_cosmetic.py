def car_race_collision(integer_number_of_cars: int) -> int:
    λψ₇₁₉ξ: int = 0
    Ϟ●₄₃₂: int = 0

    def ƛₕ₄₉₈ₘ(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return ƛₕ₄₉₈ₘ(n - 1, acc + integer_number_of_cars)

    λψ₇₁₉ξ = ƛₕ₄₉₈ₘ(integer_number_of_cars, Ϟ●₄₃₂)
    return λψ₇₁₉ξ