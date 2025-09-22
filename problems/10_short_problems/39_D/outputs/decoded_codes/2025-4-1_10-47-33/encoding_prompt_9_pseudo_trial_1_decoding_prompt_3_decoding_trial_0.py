def main():
    # Get two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of numbers
    first_numbers = first_input.split()
    second_numbers = second_input.split()
    
    # Initialize a variable to count differences
    difference_count = 0 

    # Loop through the first three numbers in both lists
    for index in range(3):
        # Convert the string numbers to integers
        first_number = int(first_numbers[index])
        second_number = int(second_numbers[index])
        
        # Check if the numbers at the same index are different
        if first_number != second_number:
            difference_count += 1
    
    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
