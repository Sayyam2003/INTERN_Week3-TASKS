#This script lists all .py files in the current directory along with their file sizes (in bytes):
import os

# List all .py files and their sizes
for filename in os.listdir():
    if filename.endswith(".py"):
        size = os.path.getsize(filename)
        print(f"{filename} - {size} bytes")

#Read Filenames from argv and Print Their Contents
#This script reads filenames from command-line arguments, opens each one, and prints its content:
import sys

# Check if files are passed
if len(sys.argv) < 2:
    print("Usage: python script.py file1.txt file2.py ...")
    sys.exit(1)

# Loop through filenames (skip the first argv which is the script name)
for filename in sys.argv[1:]:
    try:
        with open(filename, 'r') as f:
            print(f"\n--- Contents of {filename} ---")
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")
