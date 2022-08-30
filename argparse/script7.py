from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description='Demo program')
    parser.add_argument('--flag',
                        action='store_true',
                        help='when provided sets to True, otherwise False')
    parser.add_argument('--reverse-flag',
                        action='store_false',
                        help='when provided sets to False, otherwise True')

    parser.add_argument('--version', action='version', version='script6 v1.0')
    return parser


def cli():
    p = create_parser()
    args = p.parse_args()
    return args.flag, args.reverse_flag


def main():
    flag, reverse_flag = cli()
    print(flag)
    print(reverse_flag)


if __name__ == '__main__':
    main()
