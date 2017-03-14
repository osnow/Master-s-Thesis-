#!/usr/bin/env python

"""This script draws a boxplot of each atom contribution to the cavity."""


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
    parser.add_argument("filename", type=isfile,
                        help="contribution data file")
    parser.add_argument("-o", "--output",
                        help="output file name")
    parser.add_argument("-n", type=int, default=0,
                        help="show n greatest contributions")
    parser.add_argument("-s", "--stdev", action="store_true",
                        help="only plot standard deviations")
    parser.add_argument("-r", metavar="residue", nargs="+",
                        help="plot specific residues along time")
    return parser.parse_args()


def die(s):
    print >> sys.stderr, "ERROR:", s
    exit(1)


def show_usage():
    print >> sys.stderr, "usage: python " + sys.argv[0] + " <filename.dat>"


def read_contrib(fname):
    data = []
    with open(fname, "rt") as f:
        for line in f:
            split = line.split()
            k = split[0]
            counts = [int(c) for c in split[2:]]
            data.append((k, counts))
    return data


def med(x):
    x = sorted(x)
    length = len(x)
    if not length % 2:
        return (x[length / 2] + x[(length - 1) / 2]) / 2.0
    return float(x[length / 2])


def plot_sd(data):
    x = numpy.array([i+1 for i in range(len(data[0]))])
    d = numpy.std(data[1], axis=1)
    pyplot.bar(x, d)
    pyplot.xticks(x+.5, data[0], rotation=90)
    ylim = pyplot.ylim()
    pyplot.ylim((ylim[0]-10, ylim[1]+10))
    pyplot.xlim((x[0]-1, x[-1]+1))
    pyplot.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.2)
    pyplot.title("Residue contribution standard deviations")


def plot_barplot(data):
    x = [i+1 for i in range(len(data[0]))]
    pyplot.boxplot(data[1])
    pyplot.xticks(x, data[0], rotation=90)
    ylim = pyplot.ylim()
    pyplot.ylim((ylim[0]-10, ylim[1]+10))
    pyplot.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.2)
    pyplot.title("Residue contribution")


def plot_residues(data, residues):
    def running_average(x, N):
        return numpy.convolve(x, numpy.ones((N,))/N)[(N-1):]
    if "all" in residues:
        residues = data[0]
    for r in residues:
        try:
            i = data[0].index(r)
        except:
            die("No residue named '{0}'".format(r))
#        y = running_average(data[1][i], 5)
        y = data[1][i]
        pyplot.plot(y, label=r)
    pyplot.legend(loc="best")


def main():
    args = parse_args()
    data = read_contrib(args.filename)

    if args.n:
        data = sorted(data, key=lambda x: med(x[1]), reverse=True)
        data = data[:args.n]

    data = zip(*data)

    if args.r:
        plot_residues(data, args.r)
    elif args.stdev:
        plot_sd(data)
    else:
        plot_barplot(data)

    if args.output:
        pyplot.savefig(args.output)
    else:
        pyplot.show()


if __name__ == '__main__':
    main()
