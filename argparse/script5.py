from argparse import ArgumentParser


parser = ArgumentParser(description='Demo program')
parser.add_argument('--density', default=0., help='density provided as a float')

args = parser.parse_args()

print(args.density)
