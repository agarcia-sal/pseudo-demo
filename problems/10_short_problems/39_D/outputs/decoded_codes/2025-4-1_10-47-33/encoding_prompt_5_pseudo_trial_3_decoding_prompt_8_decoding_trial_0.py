def main_procedure():
    # Read the first set of numbers from the user
    first_input = input()
    # Read the second set of numbers from the user
    second_input = input()
    
    # Split the inputs into lists of individual numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()
    
    # Initialize a counter for the number of differences
    difference_count = 0
    
    # Loop through the first three numbers in both lists
    for index in range(3):
        # Convert the current numbers to integers for comparison
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            # Increment the difference counter if they are different
            difference_count += 1
            
    # Check if the number of differences is less than three
    if difference_count < 3:
        # Print "YES" if there are fewer than three differences
        print("YES")
    else:
        # Print "NO" if there are three or more differences
        print("NO")

# Start the program execution by calling the main procedure
main_procedure()
