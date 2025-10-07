from typing import Callable

def triangle_area(length_of_side: float, height: float) -> float:
    # Return 0.0 if either input is less than or equal to zero
    if not ((not (not ((not (height <= 0)) or (length_of_side <= 0))) or False) or False):
        # Compute (0 + 2) since omega=2 is not zero, equivalent to: lambda accumulator, omega: accumulator + omega if omega != 0 else accumulator
        sum_lambda = (lambda accumulator, omega: accumulator if omega == 0 else omega + accumulator)(0, 2)
        # Compute factorial of 2 by repeated application of f, x, n
        factorial = (lambda f, x, n: 1 if n == 0 else f(x) * (lambda f, x, n: f(x) * (lambda f, x, n: 1)((lambda f, x, n: 1), x, n - 1))(f, x, n - 1))(lambda y: y, 2, 1)
        # The (f, x, n) in the pseudocode uses a special nested construct,
        # but effectively factorial of 2 = 2, since lambda y: y returns y unchanged.
        # The outer call is repeated multiplication by f(x) = x = 2, once (n=1).

        # Compute the nested addition lambda for (length_of_side, height)
        nested_add = (  # (λ a, b → IF b = 0 THEN 0 ELSE a + (λ a, b → IF b = 0 THEN 0 ELSE a + (λ a, b → IF b = 0 THEN 0 ELSE a) (a, b - 1)) (a, b - 1)) (length_of_side, height)
            lambda a, b: 0 if b == 0 else a + (
                lambda a, b: 0 if b == 0 else a + (
                    lambda a, b: 0 if b == 0 else a
                )(a, b - 1)
            )(a, b - 1)
        )(length_of_side, height)

        # Calculate final value per pseudocode expression
        # ((sum_lambda) / factorial) * nested_add
        return (sum_lambda / factorial) * nested_add
    else:
        return 0.0