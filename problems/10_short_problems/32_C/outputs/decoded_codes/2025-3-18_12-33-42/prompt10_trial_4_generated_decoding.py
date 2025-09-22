def mc(n, s):
    """Calculate the transformed value based on input values n and s."""
    q = n // s  # Integer division
    r = n % s   # Modulo operation
    if r > 0:
        return r * (q + 1)
    else:
        return n

def main():
    # Read input values for n, m, s from user
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate the result by multiplying two function calls
    result = mc(n, s) * mc(m, s)
    
    # Print the result
    print(result)

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
