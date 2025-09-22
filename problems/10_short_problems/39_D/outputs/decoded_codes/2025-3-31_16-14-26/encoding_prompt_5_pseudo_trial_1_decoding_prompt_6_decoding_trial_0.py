def main():
    # Get input from the user
    first_input = input()  # Read the first line of input as a string
    second_input = input()  # Read the second line of input as a string

    # Split the input strings into lists of numbers
    first_list = first_input.split()  # Split into list of strings
    second_list = second_input.split()  # Split into list of strings
    
    # Initialize the difference counter
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Iterate from 0 to 2 (inclusive)
        # Convert the corresponding elements to integers for comparison
        first_number = int(first_list[index])  # Convert string to integer
        second_number = int(second_list[index])  # Convert string to integer
        
        # If the numbers are not equal, increase the difference counter
        if first_number != second_number:  # Check if numbers are different
            difference_count += 1  # Increment the difference counter
            
    # Check the number of differences
    if difference_count < 3:  # If there are fewer than three differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Start the program by calling the main function
main()
