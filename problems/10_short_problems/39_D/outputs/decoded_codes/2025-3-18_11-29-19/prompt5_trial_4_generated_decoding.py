def main():
    # Get two lines of input containing space-separated integers
    first_input = input()
    second_input = input()

    # Split the inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count the differences
    difference_count = 0 

    # Loop through each position of the lists
    for index in range(3):  # Looping from 0 to 2
        # Convert the current position from strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # If the numbers at the current position are different, increment the difference counter
        if first_number != second_number:
            difference_count += 1

    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
