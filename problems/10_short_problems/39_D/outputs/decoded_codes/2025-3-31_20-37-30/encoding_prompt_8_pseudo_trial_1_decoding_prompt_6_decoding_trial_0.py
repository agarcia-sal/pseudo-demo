def main():
    # Prompt the user for input values
    print("Enter first set of numbers:")
    first_input = input()  # Get user input for the first set
    print("Enter second set of numbers:")
    second_input = input()  # Get user input for the second set
    
    # Split the input strings into lists of numbers
    first_list = first_input.split()  # Convert input string into a list
    second_list = second_input.split()  # Convert input string into another list
    
    differences_count = 0  # Initialize a counter for differences

    # Loop through the first three numbers in both lists
    for index in range(3):  # Looping from 0 to 2
        first_number = int(first_list[index])  # Convert first list element to integer
        second_number = int(second_list[index])  # Convert second list element to integer
        
        # Check if the numbers are different
        if first_number != second_number:  # If numbers are not equal
            differences_count += 1  # Increment the differences count
            
    # Check the number of differences found
    if differences_count < 3:  # If count of differences is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the main function
main()
