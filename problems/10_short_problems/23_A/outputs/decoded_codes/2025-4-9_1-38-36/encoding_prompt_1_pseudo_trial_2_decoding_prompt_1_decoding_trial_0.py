# BEGIN

# Step 1: Read an input string from the user, excluding the last character (newline)
inputString = input()

# Step 2: Get the length of the input string
stringLength = len(inputString)

# Step 3: Initialize a variable to keep track of the maximum length of repeated substrings found
longestRepeatLength = 0

# Step 4: Loop through potential lengths of substrings from 0 to stringLength-1
for substringLength in range(stringLength):
  
    # Step 5: For each length, check for repeated substrings
    for startingIndex in range(stringLength):
      
        # Step 6: Attempt to find a substring starting at 'startingIndex' with length 'substringLength'
        currentSubstring = inputString[startingIndex:startingIndex + substringLength]
        
        # Ensure we don't go out of bounds when extracting the substring
        if startingIndex + substringLength <= stringLength:
          
            # Step 7: Check if this substring appears again in the input string after its starting position
            if inputString.find(currentSubstring, startingIndex + 1) != -1:
              
                # Step 8: If found, update the longest repeat length
                longestRepeatLength = substringLength
                break  # Exit the inner loop as we found a repeated substring
                
    # ENDFOR

# ENDFOR

# Step 9: Output the length of the longest repeated substring found
print(longestRepeatLength)

# END
