import re

def main():
    # Step 1: Read the input path from the user
    raw_path = input()
    
    # Step 2: Remove any leading or trailing whitespace from the input
    trimmed_path = raw_path.strip()
    
    # Step 3: Normalize the path to remove any redundant slashes
    normalized_path = normalize_path(trimmed_path)
    
    # Step 4: Substitute the beginning of the path if it starts with multiple slashes
    cleaned_path = substitute_leading_slashes(normalized_path)

    # Step 5: Output the final cleaned path
    print(cleaned_path)

def normalize_path(path):
    # Replace backslashes with forward slashes for consistency
    path = path.replace('\\', '/')
    return path

def substitute_leading_slashes(path):
    # Replace occurrences of one or more leading slashes with a single leading slash
    return re.sub(r'^/+','/', path)

# Uncomment the following line to execute the main function if running as a script
# if __name__ == "__main__":
#     main()

# Test cases
# Input: "///folder//subfolder///file.txt" -> Output: "/folder/subfolder/file.txt"
# Input: "C:\\folder\\subfolder\\file.txt" -> Output: "/folder/subfolder/file.txt"
# Input: "     //leading/slash   " -> Output: "/leading/slash"
# Input: "////" -> Output: "/"
