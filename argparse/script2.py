from argparse import ArgumentParser
from math import factorial


parser = ArgumentParser(description='Calculate the factorial of a number')
# if no type is provided the argument will be made available as a string
parser.add_argument('--factorial', type=int, help='integer')

args = parser.parse_args()

if args.factorial is not None:
    print(factorial(args.factorial))
