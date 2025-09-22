def main():
    # Receive input from the user
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter to track position differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert each string in the lists to an integer for comparison
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # If the numbers are not equal, increment the difference counter
        if first_number != second_number:
            difference_count += 1 

    # Check if the difference count is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()
