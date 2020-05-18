import argparse

# create parser object
parser = argparse.ArgumentParser(description="Interpret positional arguments.")

# add two arguments (source and destination)
parser.add_argument('source', action='store', help='The source of an operation.')
parser.add_argument('dest', action='store', help='The destination of the operation.')

# process
arguments = parser.parse_args()

# print the value of arguments
print(f"Start from {arguments.source} to {arguments.dest}")