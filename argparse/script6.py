from argparse import ArgumentParser


parser = ArgumentParser(description='Demo program')
parser.add_argument('--flag',
                    action='store_true',
                    help='when provided sets to True, otherwise False')
parser.add_argument('--reverse-flag',
                    action='store_false',
                    help='when provided sets to False, otherwise True')

parser.add_argument('--version', action='version', version='script6 v1.0')


args = parser.parse_args()

print(args.flag)
print(args.reverse_flag)
