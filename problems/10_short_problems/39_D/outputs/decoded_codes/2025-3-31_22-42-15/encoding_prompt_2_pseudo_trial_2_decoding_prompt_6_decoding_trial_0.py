# Start the program

def main():
    # Prompt the user for input and read inputs into variables
    first_input = input()
    second_input = input()
    
    # Split the input into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a variable to count the number of differences
    difference_count = 0
    
    # Compare the components from both input lists
    for index in range(3):  # Assuming inputs contain exactly 3 components
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer
        
        # Check for differences
        if first_value != second_value:
            difference_count += 1  # Increment count of differences
    
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Call the main function to execute the program
main()
