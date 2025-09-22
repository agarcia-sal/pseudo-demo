# Start of the program

# Importing the absolute function from the math module
from math import fabs

# Read input and convert it to an absolute integer
n = int(fabs(int(input())))  # Get the absolute value of the input integer
i = 0  # Initialize the counter variable

# Begin infinite loop to calculate triangular numbers
while True:
    # Calculate the triangular number for the current value of i
    s = (i * (i + 1)) // 2  # Integer division to ensure s is an integer
    m = s - n  # Calculate the difference between triangular number and input

    # Check conditions for the triangular number
    if s == n:
        print(i)  # Display the value of i
        break  # Exit the loop if s equals n
    elif s > n:
        if m % 2 == 0:  # Check if m is even
            print(i)  # Display the value of i
            break  # Exit the loop if m is even

    # Increment i by 1 for the next iteration
    i += 1  

# End of the program
