# Define a function named doMain
def doMain():
    # Prompt the user to enter the first set of values
    first_set = input()
    # Prompt the user to enter the second set of values
    second_set = input()
    
    # Split the input strings into lists of values
    first_list = first_set.split()
    second_list = second_set.split()
    
    # Initialize a counter to keep track of differences
    difference_count = 0
    
    # Loop through each index from 0 to 2
    for index in range(3):
        # Convert the values at the current index to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are not equal
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1
            
    # Check if the difference count is less than 3
    if difference_count < 3:
        # Output "YES"
        print("YES")
    else:
        # Output "NO"
        print("NO")

# Execute the doMain function when the program starts
doMain()
