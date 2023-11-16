import os
import sys

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), directory)
            print(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py /path/to/your/repo")
        sys.exit(1)

    repo_path = sys.argv[1]
    list_files(repo_path)