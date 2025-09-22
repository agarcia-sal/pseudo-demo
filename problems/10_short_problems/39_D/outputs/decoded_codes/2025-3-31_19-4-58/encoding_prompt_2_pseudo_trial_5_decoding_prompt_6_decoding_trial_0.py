# Define a function named doMain
def doMain():
    # Prompt the user to enter the first string of numbers
    first_input = input()
    # Prompt the user to enter the second string of numbers
    second_input = input()
    
    # Split the input strings into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter variable for differences
    difference_count = 0
    
    # Loop through the indices 0 to 2
    for index in range(3):
        # Convert the string at current index to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Check if the numbers are not equal
        if first_number != second_number:
            # Increase the difference count
            difference_count += 1
    
    # Check if the difference count is less than 3
    if difference_count < 3:
        print("YES")  # Output "YES"
    else:
        print("NO")   # Output "NO"

# Invoke the function to execute the program
doMain()
