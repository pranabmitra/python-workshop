import argparse

parser = argparse.ArgumentParser(description="Interpret a Boolean flag.")
# The store_true action means that the parser will set the value of the argument to True if the flag input is present. If the flag input is not present, it will set the value to False.
parser.add_argument('--flag', dest='flag', action='store_true', help='Set the flag value to True.')

arguments = parser.parse_args()

print(f"The flag's value is {arguments.flag}")