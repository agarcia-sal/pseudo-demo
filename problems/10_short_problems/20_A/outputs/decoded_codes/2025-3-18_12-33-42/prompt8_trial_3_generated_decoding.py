import re

def normalize(file_path):
    # Standardize the format by replacing backslashes with forward slashes.
    return file_path.replace('\\', '/')

def replace_leading_slashes(normalized_path):
    # Use regex to replace leading slashes with a single slash.
    return re.sub(r'^(\/+)', '/', normalized_path)

def main():
    # Step 1: Read the input path from standard input
    file_path = input().strip()
    
    # Step 2: Normalize the path
    normalized_path = normalize(file_path)
    
    # Step 3: Remove any leading slashes
    modified_path = replace_leading_slashes(normalized_path)
    
    # Step 4: Output the modified path
    print(modified_path)

if __name__ == "__main__":
    main()
