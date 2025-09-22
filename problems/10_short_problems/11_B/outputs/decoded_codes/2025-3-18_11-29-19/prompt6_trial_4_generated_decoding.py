# Get the absolute value of the user input and convert it to an integer
input_number = int(input())
target_number = abs(input_number)

# Initialize an index counter
index = 0

# Start an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2
    
    # Calculate the difference between the current sum and target number
    difference = sum_of_natural_numbers - target_number

    # Check if the current sum is equal to the target number
    if sum_of_natural_numbers == target_number:
        # If they are equal, print the current index and exit the loop
        print(index)
        break
    
    # Check if the current sum exceeds the target number
    elif sum_of_natural_numbers > target_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # If the difference is even, print the current index and exit the loop
            print(index)
            break
    
    # Increment the index for the next iteration
    index += 1
