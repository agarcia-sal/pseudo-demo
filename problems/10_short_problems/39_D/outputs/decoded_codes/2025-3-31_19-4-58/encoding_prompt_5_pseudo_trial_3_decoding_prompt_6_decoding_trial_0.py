# Define the main function
def main():
    # Read input values from the user
    first_input = input()  # Get the first set of numbers as a string
    second_input = input()  # Get the second set of numbers as a string
    
    # Split the input strings into lists of values
    first_set = first_input.split()  # Split the first input by spaces
    second_set = second_input.split()  # Split the second input by spaces
    
    # Initialize a counter for differences
    difference_count = 0  # Start the difference counter at 0

    # Compare the numerical values from both sets
    for index in range(3):  # Loop through indices 0 to 2
        first_value = int(first_set[index])  # Convert the first value to integer
        second_value = int(second_set[index])  # Convert the second value to integer
        
        # Check if the values are different
        if first_value != second_value:  # If the values do not match
            # Increment the difference counter
            difference_count += 1  # Increase the count of differences
    
    # Determine if the number of differences is less than 3
    if difference_count < 3:  # If there are fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Program execution starts here
main()  # Call the main function to execute the program
