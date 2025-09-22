def main():
    # Read two lines of input containing space-separated numbers
    inputLine1 = input()
    inputLine2 = input()

    # Split the input lines into lists of strings
    list1 = inputLine1.split()
    list2 = inputLine2.split()

    # Initialize a counter for differing elements
    differenceCount = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from strings to integers
        number1 = int(list1[index])
        number2 = int(list2[index])
        
        # Compare the corresponding elements from both lists
        if number1 != number2:
            # Increment the counter if they differ
            differenceCount += 1
            
    # Check if the count of differing elements is less than 3
    if differenceCount < 3:
        print("YES")  # There are less than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Main execution starts here
main()
