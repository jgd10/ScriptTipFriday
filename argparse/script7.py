from argparse import ArgumentParser


parser = ArgumentParser(description='Demo program')
parser.add_argument('--density', default=0.,
                    help='density provided as a float')
parser.add_argument('--bool',
                    action='store_true',
                    help='when provided sets to True, otherwise False')


args = parser.parse_args()

print(args.density)
print(args.bool)
