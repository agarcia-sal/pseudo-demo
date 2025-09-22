# Function to find the index based on the input number
def find_index():
    # Get the absolute value of an integer input
    input_number = abs(int(input()))
    
    # Initialize a variable to keep track of the index
    index = 0

    # Infinite loop to find the desired index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_natural_numbers = (index * (index + 1)) / 2
        
        # Calculate the difference between the sum and the input number
        difference = sum_of_natural_numbers - input_number
        
        # Check if the sum equals the input number
        if sum_of_natural_numbers == input_number:
            # Print the current index and exit the loop
            print(index)
            break
        
        # Check if the sum is greater than the input number
        elif sum_of_natural_numbers > input_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                # Print the current index and exit the loop
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute the logic
find_index()
