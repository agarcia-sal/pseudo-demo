def find_natural_number(n):
    # Validate input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    i = 0  # Initialize i

    while True:
        # Calculate the sum of the first 'i' natural numbers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the calculated sum and 'n'
        m = s - n

        # Check if the sum equals 'n'
        if s == n:
            print(i)  # Output the value of 'i'
            break

        # Check if the sum exceeds 'n'
        elif s > n:
            # Check if the difference 'm' is even
            if m % 2 == 0:
                print(i)  # Output the value of 'i'
                break
        
        # Increment 'i' for the next iteration
        i += 1

# Example usage
if __name__ == "__main__":
    n = int(input())  # Assume the user inputs a non-negative integer
    find_natural_number(n)
