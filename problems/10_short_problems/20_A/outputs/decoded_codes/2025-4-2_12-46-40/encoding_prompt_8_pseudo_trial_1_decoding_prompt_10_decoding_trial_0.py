import posixpath
import sys
import re

def normalize_path(input_path):
    # Normalize the path using posixpath
    normalized_path = posixpath.normpath(input_path)
    
    # Ensure that the path starts with exactly one forward slash
    final_path = re.sub(r'^/+','/', normalized_path)
    
    return final_path

def main():
    # Step 2: Read input path
    input_path = input().strip()
    
    # Step 3: Normalize the path
    final_path = normalize_path(input_path)
    
    # Step 5: Output the final path
    print(final_path)

if __name__ == "__main__":
    main()
