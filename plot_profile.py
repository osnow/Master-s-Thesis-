#!/usr/bin/env python

"""This script plots the minimum, maximum and average profile from a
profile file passed to command-line."""

import sys

if sys.version < "2.7":
    print >> sys.stderr, "ERROR: This script requires Python 2.7.x. "\
                         "Please install it and try again."
    exit(1)

try:
    import matplotlib.pyplot as pyplot
    import numpy
except ImportError:
    print >> sys.stderr, "ERROR:",
    print >> sys.stderr, "This script requires matplotlib and numpy. "\
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
    parser.add_argument("filename", nargs="+", type=isfile,
                        help="contribution data file")
    parser.add_argument("-o", "--output", help="output file name")
    return parser.parse_args()


def plot(fname):
    with open(fname, "rt") as f:
        z = [float(v) for v in f.next().split()]
        data = [[float(v) for v in line.split()] for line in f]
    data = zip(*data)
    data = numpy.array(data)
    
    # if the data file contains more that 1 frame
    if data.shape[1] > 1:
        amax = numpy.max(data[1:], axis=1)
        amin = numpy.min(data[1:], axis=1)
        aave = numpy.average(data[1:], axis=1)

        pyplot.fill_between(z, amin, amax, color="#C7C7C7")
        pyplot.plot(z, aave, color="k", lw=2, label=fname)

    else:
        r = data[1:]
        pyplot.plot(z, r, label=fname)


def main():
    args = parse_args()
    for fn in args.filename:
        plot(fn)
    pyplot.xlabel("Z")
    pyplot.ylabel("Radius (Angstrom)")
    pyplot.legend(loc="best")
    if args.output:
        pyplot.savefig(args.output)
    else:
        pyplot.show()



if __name__ == '__main__':
    main()
