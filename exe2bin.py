#!/usr/bin/env python3

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Parser")
    parser.add_argument("-i", nargs='+', help="Input file name")
    parser.add_argument("-o", nargs='+', help="Output file name")
    args = parser.parse_args()

    if args.i == None or args.o == None:
        print("Missing argument")
        parser.print_help()
        sys.exit(1)

    ifile = args.i[0]
    ofile = args.o[0]

    print("i={}".format(ifile))
    print("o={}".format(ofile))

    with open(ifile, "rb") as f:
        ibytes = f.read()
        pattern = b'\x55\xAA\x5A\xA5\xc2\x00\x00\x00\x01\x00\x00\x00\x48\x57\x45\x57\x31\x31\x2e\x31'
        off = ibytes.find(pattern) - 92

        if off < 0:
            print("Could not found pattern")
            sys.exit(1)

        print("off={}\nolength={}".format(off, len(ibytes) - off))

        with open(ofile, "wb") as w:
            w.write(ibytes[off:])

if __name__ == "__main__":
    main()
