def find_matching_value():
    # Read an integer input and get its absolute value
    n = abs(int(input()))

    # Initialize a counter variable
    i = 0

    # Infinite loop to find the desired value
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2

        # Calculate the difference between s and n
        m = s - n

        # Check if the current sum equals n
        if s == n:
            print(i)  # Found the solution, print i
            break

        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Found the solution, print i
                break

        # Increment i for the next iteration
        i += 1

# Example test cases that can be uncommented for testing
# find_matching_value()  # Input: 0, Output: 0
# find_matching_value()  # Input: 3, Output: 3
# find_matching_value()  # Input: 5, Output: 5
