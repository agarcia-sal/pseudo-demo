Set variable input_string to read a line from the standard input and remove leading and trailing whitespace


input_string = input().strip()


Replace all occurrences of the substring "dot" in input_string with "." (a period)
Replace all occurrences of the substring "at" in input_string with "@" (at symbol)


input_string = input_string.replace("dot", ".").replace("at", "@")


If the first character of input_string is ".":
    Prepend "dot" to input_string, excluding the first character


if input_string.startswith('.'):
    input_string = "dot" + input_string[1:]


Set variable count_at to 0
Create an empty list result_list
Set variable length to 0 (this variable is defined but not used)


count_at = 0
result_list = []
length = 0  # This variable is defined but not used.


If the first character of input_string is "@":
    Prepend "at" to input_string, excluding the first character


if input_string.startswith('@'):
    input_string = "at" + input_string[1:]


For each character char in input_string:
    If char is "@" (at symbol):
        If count_at is greater than 0:
            Append the substring "at" to result_list
        Otherwise:
            Append "@" to result_list
        Set count_at to 1
    Otherwise:
        Append char to result_list


for char in input_string:
    if char == '@':
        if count_at > 0:
            result_list.append("at")
        else:
            result_list.append("@")
        count_at = 1
    else:
        result_list.append(char)


Set variable final_string to join all elements in result_list into a single string


final_string = ''.join(result_list)


If the last character of final_string is ".":
    Remove the last character and append "dot" to final_string


if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"


Print final_string


print(final_string)


input_string = input().strip()
input_string = input_string.replace("dot", ".").replace("at", "@")

if input_string.startswith('.'):
    input_string = "dot" + input_string[1:]

count_at = 0
result_list = []

if input_string.startswith('@'):
    input_string = "at" + input_string[1:]

for char in input_string:
    if char == '@':
        if count_at > 0:
            result_list.append("at")
        else:
            result_list.append("@")
        count_at = 1
    else:
        result_list.append(char)

final_string = ''.join(result_list)

if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"

print(final_string)
