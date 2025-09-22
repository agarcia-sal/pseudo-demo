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
    for index in range(3):  # Looping from 0 to 2
        number1 = int(list1[index])  # Convert to integer
        number2 = int(list2[index])  # Convert to integer
        
        # Check if the numbers are different
        if number1 != number2:  # If numbers are not equal
            difference_count += 1  # Increment the difference count

    # Determine if the difference count is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
