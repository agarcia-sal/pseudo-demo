def main():
    # Read two lines of input representing two sets of numbers
    first_set = input()  # First line of input
    second_set = input()  # Second line of input
    
    # Split the input strings into lists of numbers
    list1 = first_set.split()  # Split the first input line into a list of strings
    list2 = second_set.split()  # Split the second input line into a list of strings
    
    # Initialize a counter for differences
    difference_count = 0  # Counter for differences between the two lists
    
    # Compare corresponding elements from both lists
    for index in range(3):  # Loop through indices 0 to 2
        number1 = int(list1[index])  # Convert the current element from list1 to an integer
        number2 = int(list2[index])  # Convert the current element from list2 to an integer
        
        # Check if the numbers are different
        if number1 != number2:  # If the numbers are not equal
            difference_count += 1  # Increment the difference count
            
    # Determine if the difference count is less than 3
    if difference_count < 3:  # If the number of differences is less than 3
        print("YES")  # Print "YES"
    else: 
        print("NO")  # Print "NO"

# Execute the main function
main()
