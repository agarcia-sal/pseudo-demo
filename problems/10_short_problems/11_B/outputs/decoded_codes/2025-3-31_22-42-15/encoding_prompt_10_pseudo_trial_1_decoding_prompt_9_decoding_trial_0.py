# Start the program
# Declare the variables
n = abs(int(input()))  # Set variable n to the absolute value of the integer input
i = 0  # Initialize i to 0

while True:  # Begin infinite loop
    # Calculate the triangular number s
    s = (i * (i + 1)) // 2  # Use integer division for triangular number
    m = s - n  # Calculate the difference

    # Check conditions
    if s == n:  # If s equals n
        print(i)  # Display the value of i
        break  # Exit the loop
    elif s > n:  # Else if s is greater than n
        if m % 2 == 0:  # If m is an even number
            print(i)  # Display the value of i
            break  # Exit the loop

    i += 1  # Increment i by 1
