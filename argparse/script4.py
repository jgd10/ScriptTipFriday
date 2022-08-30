from argparse import ArgumentParser


parser = ArgumentParser(description='Divide by 3')
parser.add_argument('--num1', type=float, help='Option 1')
parser.add_argument('--num2', type=float, help='Option 2')


args = parser.parse_args()

if args.num1 is not None:
    print(args.num1/3.)


if args.num2 is not None:
    print(args.num2/3.)
