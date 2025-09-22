def main_function():
    # Read two lines of input from the user representing two sets of numbers
    first_input = input()
    second_input = input()

    # Split the input strings into lists of numbers
    numbers_from_first_input = first_input.split()
    numbers_from_second_input = second_input.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three numbers from both inputs
    for index in range(3):
        # Convert the current number from the first input to an integer
        number_from_first_input = int(numbers_from_first_input[index])
        
        # Convert the current number from the second input to an integer
        number_from_second_input = int(numbers_from_second_input[index])
        
        # Check if the numbers from both inputs are different
        if number_from_first_input != number_from_second_input:
            # Increment the difference counter
            difference_count += 1

    # Evaluate the total number of differences
    if difference_count < 3:
        # Output "YES" if there are fewer than three differences
        print("YES")
    else:
        # Output "NO" if there are three or more differences
        print("NO")

# Call the main function to execute the comparison
main_function()
