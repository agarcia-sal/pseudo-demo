def mc(value, step):
    # Calculate the quotient and remainder when value is divided by step
    quotient = value // step
    remainder = value % step

    # If there is a remainder, return (remainder * (quotient + 1)), otherwise return value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

def main():
    # Read input values n, m, and s from the user
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate the result using the mc function for n and m, then multiply the results
    result = mc(n, s) * mc(m, s)
    print(result)

# Entry point for the program
if __name__ == "__main__":
    main()
