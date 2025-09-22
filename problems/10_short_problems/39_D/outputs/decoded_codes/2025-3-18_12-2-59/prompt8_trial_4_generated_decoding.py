def main_function():
    # Accept two input strings from the user
    user_input1 = input()
    user_input2 = input()
    
    # Split the input strings into lists of numbers
    list_of_numbers1 = user_input1.split()
    list_of_numbers2 = user_input2.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three numbers in both lists
    for index in range(3):
        # Convert the current number from both lists to integers
        number1 = int(list_of_numbers1[index])
        number2 = int(list_of_numbers2[index])
        
        # Check if the numbers are different
        if number1 != number2:
            # Increment the difference counter
            difference_count += 1
    
    # Check the total number of differences
    if difference_count < 3:
        print("YES")  # Output indicating fewer than 3 differences
    else:
        print("NO")   # Output indicating 3 or more differences

# Start the program by calling the main function
if __name__ == "__main__":
    main_function()
