# Start of the program
# Read the input number and assign its absolute value to 'n'
n = abs(int(input()))

# Initialize a counter 'i' to zero
i = 0

# Begin an infinite loop to explore potential solutions
while True:
    # Calculate the sum of the first 'i' numbers
    sumOfFirsti = (i * (i + 1)) / 2
    
    # Calculate the difference between sumOfFirsti and n
    difference = sumOfFirsti - n
    
    # Check if the sum equals the input number
    if sumOfFirsti == n:
        # Output the current value of 'i'
        print(i)
        # Exit the loop
        break
    
    # Check if the sum exceeds the input number
    elif sumOfFirsti > n:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # Output the current value of 'i'
            print(i)
            # Exit the loop
            break
    
    # Increment the counter to check the next number
    i += 1
# End of program
