def main():
    # Receive input from the user
    first_input = input()  # Input from the user for first set of numbers
    second_input = input() # Input from the user for second set of numbers
    
    # Split the input strings into lists of strings
    first_list = first_input.split()  # Splitting first input by spaces
    second_list = second_input.split()  # Splitting second input by spaces
    
    # Initialize a counter to track position differences
    difference_count = 0  # Counter for differences between the two lists
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Only considering the first three elements
        # Convert each string in the lists to an integer for comparison
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer
        
        # If the numbers are not equal, increment the difference counter
        if first_number != second_number:
            difference_count += 1  # Increment difference count if numbers differ
    
    # Check if the difference count is less than 3
    if difference_count < 3:
        print("YES")  # Print "YES" if fewer than 3 differences
    else:
        print("NO")  # Print "NO" if 3 or more differences

# Start the program execution
main()
