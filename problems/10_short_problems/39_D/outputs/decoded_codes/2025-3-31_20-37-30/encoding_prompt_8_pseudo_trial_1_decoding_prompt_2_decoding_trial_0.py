def main():
    # Prompt the user for input values
    print("Enter first set of numbers:")
    first_input = input()
    print("Enter second set of numbers:")
    second_input = input()
    
    # Split the input strings into lists of numbers
    first_list = first_input.split()
    second_list = second_input.split()
    
    differences_count = 0  # Initialize a counter for differences

    # Loop through the first three numbers in both lists
    for index in range(3):
        first_number = int(first_list[index])  # Convert to integer
        second_number = int(second_list[index])  # Convert to integer
        
        # Check if the numbers are different
        if first_number != second_number:
            differences_count += 1  # Increment differences count
            
    # Check the number of differences found
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
