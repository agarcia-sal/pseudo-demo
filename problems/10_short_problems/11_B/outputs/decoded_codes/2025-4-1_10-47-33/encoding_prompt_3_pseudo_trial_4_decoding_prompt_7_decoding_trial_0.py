# Start of the program
# Input: a non-negative integer 'n'
n = abs(int(input()))  # Read the input number and assign its absolute value to 'n'

# Initialize a counter 'i' to zero
i = 0  # Set i to 0

# Begin an infinite loop to explore potential solutions
while True:  # Repeat indefinitely
    # Calculate the sum of the first 'i' numbers
    sumOfFirsti = (i * (i + 1)) // 2  # Using integer division for sum of first i numbers
    
    # Calculate the difference between sumOfFirsti and n
    difference = sumOfFirsti - n  # Assign the difference to sumOfFirsti - n
    
    # Check if the sum equals the input number
    if sumOfFirsti == n:  # If sumOfFirsti is equal to n
        print(i)  # Output the current value of i
        break  # Exit the loop
    
    # Check if the sum exceeds the input number
    elif sumOfFirsti > n:  # Else if sumOfFirsti is greater than n
        # Check if the difference is an even number
        if difference % 2 == 0:  # If difference is even
            print(i)  # Output the current value of i
            break  # Exit the loop
    
    # Increment the counter to check the next number
    i += 1  # Increment i by 1

# End of program
