def main():
    # Read two lines of input representing two sets of numbers
    firstSet = input()
    secondSet = input()
    
    # Split the input strings into lists of numbers
    list1 = firstSet.split()
    list2 = secondSet.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding elements from both lists
    for index in range(3):
        number1 = int(list1[index])
        number2 = int(list2[index])
        
        # Check if the numbers are different
        if number1 != number2:
            differenceCount += 1
            
    # Determine if the difference count is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()


   Input:
   1 2 3
   1 2 3
   Output:
   YES
   

   Input:
   1 2 3
   1 4 3
   Output:
   YES
   

   Input:
   1 2 3
   4 5 3
   Output:
   YES
   

   Input:
   1 2 3
   4 5 6
   Output:
   NO
   

   Input:
   1 2 3
   1 a 3
   Output:
   (Expect an exception or error handling)
   