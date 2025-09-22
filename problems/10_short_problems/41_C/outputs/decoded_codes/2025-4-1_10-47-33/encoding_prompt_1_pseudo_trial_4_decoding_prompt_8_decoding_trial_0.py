# Begin program

# 1. Read input string from standard input and remove any leading or trailing whitespace.
input_string = input().strip()

# 2. Replace all occurrences of the substring "dot" with the character "." in the input string.
modified_string = input_string.replace("dot", ".")

# 3. Replace all occurrences of the substring "at" with the character "@" in the updated string.
modified_string = modified_string.replace("at", "@")

# 4. If the first character of the modified string is a ".", then prepend the substring "dot" to the string, excluding the first character.
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# 5. Initialize a counter "co" to track the number of consecutive "@" found.
co = 0

# 6. Initialize an empty list "c" to hold processed characters.
c = []

# 7. Initialize a variable "l" to 0 (though it is not used further in the logic).
l = 0

# 8. If the first character of the modified string is "@", then prepend the substring "at" to the string, excluding the first character.
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# 9. For each character "i" in the modified string:
for i in modified_string:
    # a. If the character "i" is an "@"
    if i == "@":
        # i. If "co" is greater than 0
        if co > 0:
            # Append the substring "at" to the list "c"
            c.append("at")
            co = 1
        else:
            # Append the character "@" to the list "c"
            c.append("@")
            co = 1
    else:
        # b. Else
        c.append(i)
        co = 0  # Reset counter for non-@ characters

# 10. Join all characters in the list "c" into a single string.
final_string = ''.join(c)

# 11. If the last character of the final string "c" is a ".", then replace the last character with the substring "dot".
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# 12. Print the final processed string "c".
print(final_string)

# End program
