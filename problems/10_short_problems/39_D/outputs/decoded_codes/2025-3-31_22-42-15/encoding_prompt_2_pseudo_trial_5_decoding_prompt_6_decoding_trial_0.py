# Start the program

def do_main():
    # Read the first input line and store it as first_input
    first_input = input()
    
    # Read the second input line and store it as second_input
    second_input = input()
    
    # Split first_input into a list of strings and store it as first_list
    first_list = first_input.split()
    
    # Split second_input into a list of strings and store it as second_list
    second_list = second_input.split()
    
    # Initialize a variable mismatch_count to zero to keep track of differences
    mismatch_count = 0

    # For each index from 0 to 2 (inclusive):
    for index in range(3):
        # Retrieve value from first_list at the current index and convert it to an integer
        first_value = int(first_list[index])
        
        # Retrieve value from second_list at the current index and convert it to an integer
        second_value = int(second_list[index])
        
        # If first_value is not equal to second_value:
        if first_value != second_value:
            # Increment mismatch_count by 1
            mismatch_count += 1

    # If mismatch_count is less than 3:
    if mismatch_count < 3:
        # Output "YES"
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# If this script is being run directly (not imported as a module):
if __name__ == "__main__":
    do_main()  # Call the do_main function to begin execution of the program
