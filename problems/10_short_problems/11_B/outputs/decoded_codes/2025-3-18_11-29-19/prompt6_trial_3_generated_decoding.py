# Start of the program

# Read an integer input and convert it to its absolute value
number = abs(int(input()))

# Initialize a counter variable
index = 0

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first 'index' natural numbers
    total_sum = (index * (index + 1)) // 2  # Using integer division
    
    # Determine the difference between the calculated sum and the input number
    difference = total_sum - number

    # Check if the total_sum equals the input number
    if total_sum == number:
        # If so, print the index and exit the loop
        print(index)
        break

    # Check if the total_sum is greater than the input number
    elif total_sum > number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # If so, print the index and exit the loop
            print(index)
            break

    # Increment the index for the next iteration
    index += 1

# End of the program
