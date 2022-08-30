from argparse import ArgumentParser


parser = ArgumentParser(description='Calculate the power of a number')
parser.add_argument('--base', type=float, help='base number')
parser.add_argument('--exponent', type=float,
                    help='exponent, can be float or negative')


args = parser.parse_args()

if args.base is not None and args.exponent is not None:
    print(args.base ** args.exponent)
