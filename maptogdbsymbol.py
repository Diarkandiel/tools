#/usr/bin/python3.8
# -*- coding: utf-8 -*-

'''
This script generates a gdb script file from a map file containing symbols and addresses of a binary. 
The gdb script sets symbol addresses in gdb for various purposes such as debugging, reverse engineering, and testing.
Usage: ./generate_gdb_script.py <map_file> <output_file>
Example: ./generate_gdb_script.py test.map gdb_script.txt
The gdb script automates setting symbol addresses in gdb for different tasks including debugging and testing.
'''

import re  # Import the regular expression module for pattern matching
import sys  # Import the sys module for system-specific parameters and functions

def parse_map_file(map_file):
    # Open the specified map file and read all the lines into a list
    with open(map_file, 'r') as f:
        lines = f.readlines()

    symbols = []
    # Iterate through each line in the list of lines
    for line in lines:
        # Match the pattern of hexadecimal addresses and symbols in the line
        match = re.match(r"^\s*([0-9A-Fa-f]+):([0-9A-Fa-f]+)\s+(\S+)$", line)
        if match:
            address = match.group(2)  # Get the hexadecimal address from the matched pattern
            symbol = match.group(3)   # Get the symbol from the matched pattern
            symbols.append((address, symbol))  # Append the address and symbol as a tuple to the symbols list

    return symbols

def generate_gdb_script(symbols, output_file):
    # Open the output file in write mode
    with open(output_file, 'w') as f:
        # Iterate through the list of symbols
        for address, symbol in symbols:
            # Write gdb commands to set symbol addresses in the gdb script file
            f.write(f"set ${{symbol}} = 0x{address}\n")

def main(sys.argv[1], sys.argv[2]):
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <map_file> <output_file>")
        sys.exit(1)  # Exit the program with error code 1

    map_file = sys.argv[1]    # Get the map file path from command line arguments
    output_file = sys.argv[2]  # Get the output file path from command line arguments
    symbols = parse_map_file(map_file)  # Parse the map file to extract symbols and addresses
    generate_gdb_script(symbols, output_file)  # Generate a gdb script file using the symbols
    print(f"Generated gdb script: {output_file}")  # Print the path to the generated gdb script

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])  # Execute the main function with command line arguments
