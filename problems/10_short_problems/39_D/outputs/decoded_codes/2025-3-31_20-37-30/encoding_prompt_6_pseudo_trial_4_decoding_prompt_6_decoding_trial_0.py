def main():
    # Step 1: Get two lines of input from the user
    first_string = input()  # First input string
    second_string = input()  # Second input string

    # Step 2: Split the input strings into lists of numbers
    first_list = first_string.split()  # Convert first input string to list of substrings
    second_list = second_string.split()  # Convert second input string to list of substrings

    # Step 3: Initialize a counter to track differences
    difference_count = 0 

    # Step 4: Compare the numbers in each list
    for index in range(3):  # Loop through the first three elements
        first_number = int(first_list[index])  # Convert first number to integer
        second_number = int(second_list[index])  # Convert second number to integer
        
        # Step 5: Check if the numbers are different
        if first_number != second_number:  # Compare the two numbers
            difference_count += 1  # Increment the difference count if they are not equal

    # Step 6: Determine if the number of differences is less than 3
    if difference_count < 3:  
        print("YES")  # Print YES if differences are less than 3
    else: 
        print("NO")  # Print NO if differences are 3 or more

# Start the program by calling the main function
main()
