def main():
    # Accept two inputs representing two sets of numbers
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter to track the number of differences
    difference_count = 0 

    # Loop through each number in the first three positions
    for index in range(3):
        # Convert the current numbers from string to integer
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are different
        if first_number != second_number:
            # Increment the difference counter
            difference_count += 1 
    
    # Determine the result based on the number of differences
    if difference_count < 3:
        print("YES")  # If differences are fewer than 3
    else:
        print("NO")   # If differences are 3 or more

# Execute the main function when the script is run
main()
