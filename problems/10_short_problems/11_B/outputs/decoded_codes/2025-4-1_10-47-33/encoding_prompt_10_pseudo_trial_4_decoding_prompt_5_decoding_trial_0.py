# Function to find the value of i based on the sum of the first i integers
def find_matching_integer():
    # Initialize n as the absolute value of the integer input
    n = abs(int(input()))
    # Set i to 0
    i = 0

    # Loop indefinitely until a condition is met to break
    while True:
        # Calculate the sum s as the sum of the first i integers
        s = i * (i + 1) // 2
        # Calculate the difference m as s - n
        m = s - n

        # Check if s is equal to n
        if s == n:
            print(i)  # Print the value of i
            break  # Terminate the loop

        # Check if s is greater than n
        elif s > n:
            # Check if m is even
            if m % 2 == 0:
                print(i)  # Print the value of i
                break  # Terminate the loop

        # Increment i by 1 for the next iteration
        i += 1

# Example of usage (uncomment to run)
# find_matching_integer()

# Edge case tests (should handle input of 0 and positive integers)
# Input: 0 should ideally output 0
# Input: 3 should output 2
# Input: 6 should output 3
