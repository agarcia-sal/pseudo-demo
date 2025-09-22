def main():
    # Read two lines of input containing space-separated numbers
    inputLine1 = input()
    inputLine2 = input()

    # Split the input lines into lists of strings
    list1 = inputLine1.split()  # Split by spaces
    list2 = inputLine2.split()  # Split by spaces

    # Initialize a counter for differing elements
    differenceCount = 0 

    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert the current elements from strings to integers
        number1 = int(list1[index])  # Convert to integer
        number2 = int(list2[index])  # Convert to integer
        
        # Compare the corresponding elements from both lists
        if number1 != number2:  # Check for difference
            # Increment the counter if they differ
            differenceCount += 1  # Increase count of differences

    # Check if the count of differing elements is less than 3
    if differenceCount < 3:  # If differences are fewer than 3
        print("YES")  # Print YES if there are less than 3 differences
    else: 
        print("NO")   # Print NO if there are 3 or more differences

# Main execution starts here
main()


     1 2 3
     1 2 3
     

     YES
     

     1 2 3
     1 5 3
     

     YES
     

     1 2 3
     4 5 6
     

     NO
     

       1 3
       1 2
       