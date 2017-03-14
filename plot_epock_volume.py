#!/usr/bin/env python

"""This script draws a timeline plot of each pocket volume 
in each file passed to command-line."""

import sys
import pandas as pd
if sys.version < "2.7":
    print >> sys.stderr, "ERROR: This script requires Python 2.7.x. "\
                         "Please install it and try again."
    exit(1)

try:
    import matplotlib.pyplot as pyplot
except ImportError:
    print >> sys.stderr, "ERROR:",
    print >> sys.stderr, "This script requires matplotlib. "\
                         "Please make sure you installed it and that "\
                         "your PYTHONPATH is set adequately."
    exit(1)


def parse_args():
    import argparse
    import os.path

    def isfile(path):
        Error = argparse.ArgumentTypeError
        if not os.path.exists(path):
            raise Error("No such file: '{0}'".format(path))
        elif not os.path.isfile(path):
            raise Error("Not a valid file: '{0}'".format(path))
        return path

    hf = lambda prog: argparse.HelpFormatter(prog, max_help_position=50)
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=hf)
    parser.add_argument("filename", type=isfile, nargs="+",
                        help="volume data file")
    parser.add_argument("-o", "--output", help="output file name")
    return parser.parse_args()


def read_data(fname):
    with open(fname, "rt") as f:
        headers = f.next().split()
        data = [[float(v) for v in line.split()] for line in f]
    return dict(zip(headers, zip(*data)))


def plot_file(fname):
    data = read_data(fname)
    x = data.pop("Time")
    for label, y in data.iteritems():
        pyplot.plot(x, pd.Series.rolling(pd.Series(list(y)),
        window=20).mean(), label=fname + " - " + label)


def main():
    args = parse_args()

    for fn in args.filename:
        plot_file(fn)

    pyplot.legend(loc="best")
    pyplot.xlabel("Time (ps)")
    pyplot.ylabel("Volume (Angstrom^3)")

    if args.output:
        pyplot.savefig(args.output)
    else:
        pyplot.show()


if __name__ == '__main__':
    main()
