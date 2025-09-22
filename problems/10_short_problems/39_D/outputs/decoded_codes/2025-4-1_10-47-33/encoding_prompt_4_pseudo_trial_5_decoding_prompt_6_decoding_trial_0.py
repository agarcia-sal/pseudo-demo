def main():
    # Read two lines of input representing two sets of numbers
    first_set = input()
    second_set = input()
    
    # Split the input strings into lists of numbers
    list1 = first_set.split()
    list2 = second_set.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Compare corresponding elements from both lists
    for index in range(3):  # Loop for first three indices
        number1 = int(list1[index])  # Convert the first number to an integer
        number2 = int(list2[index])  # Convert the second number to an integer
        
        # Check if the numbers are different
        if number1 != number2:
            difference_count += 1  # Increment the difference count if numbers are not equal
            
    # Determine if the difference count is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
