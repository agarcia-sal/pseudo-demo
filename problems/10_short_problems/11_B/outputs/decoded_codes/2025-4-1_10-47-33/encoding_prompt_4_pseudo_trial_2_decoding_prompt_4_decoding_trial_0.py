# Importing the necessary library for absolute value function
import sys

def find_integer(n):
    # Ensure that the input is non-negative
    n = abs(n)

    # Initialize the counter variable
    i = 0

    # Loop indefinitely to find the required i
    while True:
        # Calculate the sum of the first 'i' natural numbers using the formula
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        m = s - n

        # Check if the sum equals the input number
        if s == n:
            print(i)  # Output the current counter
            break  # Exit loop

        # Check if the sum exceeds the input number
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the current counter
                break  # Exit loop

        # Increment the counter for the next iteration
        i += 1

# Read an integer input
n = int(input())

# Call the function with the input value
find_integer(n)
