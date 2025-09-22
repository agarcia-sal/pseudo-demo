def mc(n, s):
    """Compute a modified value based on division."""
    q, r = divmod(n, s)  # Get quotient and remainder
    if r > 0:
        return r * (q + 1)  # Return adjusted value if there's a remainder
    else:
        return n  # Return original value if no remainder

def main():
    """Main block to read input and calculate product."""
    try:
        # Read three space-separated integers from input
        n, m, s = map(int, input().split())
        
        if s == 0:
            raise ValueError("s must not be zero.")  # Prevent division by zero

        # Calculate the results
        result1 = mc(n, s)
        result2 = mc(m, s)

        # Print the product of both results
        print(result1 * result2)

    except ValueError as e:
        print(f"Input error: {e}")  # Handle invalid input gracefully

if __name__ == "__main__":
    main()
