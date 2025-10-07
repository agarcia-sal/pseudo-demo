def derivative(coefficients):
    """
    Compute the derivative of a polynomial represented by a list of coefficients.

    Parameters:
        coefficients (list): List of polynomial coefficients, where the index represents the power of x.

    Returns:
        list: Coefficients of the derivative polynomial.
    """
    # Multiply each coefficient by its corresponding power (index), skipping the constant term at index 0
    return [index * coeff for index, coeff in enumerate(coefficients) if index > 0]