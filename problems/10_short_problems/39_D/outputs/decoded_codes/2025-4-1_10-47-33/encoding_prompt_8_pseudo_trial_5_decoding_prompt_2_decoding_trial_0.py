def main():
    # Read two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the two numbers are different
        if first_number != second_number:
            # Increment the counter for differences
            difference_count += 1
    
    # Check if the total differences are less than three
    if difference_count < 3:
        print("YES")  # Fewer than three differences
    else:
        print("NO")   # Three or more differences

# Main entry point of the program
if __name__ == "__main__":
    main()
