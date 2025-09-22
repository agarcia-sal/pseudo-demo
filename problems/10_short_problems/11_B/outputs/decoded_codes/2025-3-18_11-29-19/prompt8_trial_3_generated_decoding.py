# Get User Input
number = abs(int(input()))

# Initialize Counter
counter = 0

# Start Infinite Loop
while True:
    # Calculate sum of first i natural numbers
    sum_of_first_i = counter * (counter + 1) // 2
    # Calculate difference
    difference = sum_of_first_i - number

    # Check Conditions
    if sum_of_first_i == number:
        print(counter)
        break
    elif sum_of_first_i > number:
        if difference % 2 == 0:
            print(counter)
            break

    # Increment Counter
    counter += 1
