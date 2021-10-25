import argparse
import sys

from src.dataGene import dataGene

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='pass the input JSON schema file path')

    parser.add_argument('-n', '--num-records', help='pass the number records')

    parser.add_argument('-fmt', '--format', help='output file format')

    parser.add_argument('-o', '--outfile', help='output file name')

    args = parser.parse_args()

    dataGene(args.file, args.num_records, args.format, args.outfile)

if __name__ == "__main__":
    sys.exit(main())

