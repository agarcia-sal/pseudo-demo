# Start by getting a number from the user
target_number = int(input())  # Convert the input to an integer
target_number = abs(target_number)  # Get the absolute value and store it as target_number

# Initialize a counter variable index to 0
index = 0

# Enter an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    sum_of_first_index = (index * (index + 1)) // 2  # Using integer division

    # Calculate difference as the result of subtracting target_number from sum_of_first_index
    difference = sum_of_first_index - target_number

    # Check if the current sum equals the target number
    if sum_of_first_index == target_number:
        print(index)  # Print the value of index and exit the loop
        break

    # Check if the current sum exceeds the target number
    if sum_of_first_index > target_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Print the value of index and exit the loop
            break

    # Increment the counter variable index by 1
    index += 1  # Repeat the loop
