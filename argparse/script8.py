"""
This cell contains a very basic CLI for a jupyter notebook. To test it, run this cell and enter

--show "Hello World!"

in the prompt
"""
import argparse
import shlex

# Create the parser
import sys

parser = argparse.ArgumentParser()

# Add a flag/argument to the parser
parser.add_argument('--show', help='prints to screen whichever argument is provided')

# Take the user's input in lieu of the command line inputs

# Our input is a string and it needs to be a list of arguments for parse_args to understand it
# We use the builtin library shlex to split the string by space, whilst preserving substrings in quotes
print(sys.argv)
if not sys.argv[1:]:
    user_input = input('Enter CLI flags and args:')
    user_input = shlex.split(user_input)
    # parse the arguments we've provided
    args = parser.parse_args(user_input)
else:
    args = parser.parse_args()

# print the value supplied for the --show flag
print(args.show)
