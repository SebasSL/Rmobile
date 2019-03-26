import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--ind', dest='ind', action='store',
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.ind)