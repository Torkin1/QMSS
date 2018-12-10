"""
File name: profiler.py
Authors: Mihai Jianu, Daniele La Prova, Lorenzo Mei
Python version: 3.x
Script di profiling per gli algoritmi di ordinamento
$ python3 -m profiler -h
usage: python -m main [-h] [-m] [-r] [-d] [-o] size range
profiles quickSelectionSort execution time with major sorting algorithms
positional arguments:
  size                 size of the list
  range                maximum range of values generated
optional arguments:
  -h, --help           show this help message and exit
  -m, --median         includes quickSelectSort with sampleMedianSelect
  -r, --random         inlcudes quickSelectSort with quickSelectRand
  -d, --deterministic  includes quickSelectSort with quickSelectDet
  -o, --others         inlcudes major sorting algorithms
"""
from sys import argv
import QMSS_module
import argparse
from cProfile import run
import pstats
from random import randint
from sorting.Sorting import *
import matplotlib.pyplot as plt
import numpy as np
from math import ceil


if __name__ == "__main__":

    parser = argparse.ArgumentParser("$ python3 -m profiler",
                                     epilog="written by Mihai Jianu, Daniele La Prova, Lorenzo Mei",
                                     description="profiles quickSelectionSort execution time with major sorting algorithms")

    parser.add_argument("-m", "--median", help="includes quickSelectSort with sampleMedianSelect", action="store_true")
    parser.add_argument("-r", "--random", help="inlcudes quickSelectSort with quickSelectRand", action="store_true")
    parser.add_argument("-d", "--deterministic", help="includes quickSelectSort with quickSelectDet",
                        action="store_true")
    parser.add_argument("-o", "--others", help="inlcudes major sorting algorithms", action="store_true")
    parser.add_argument("size", type=int, help="size of the list")
    parser.add_argument("range", type=int, help="maximum range of values generated")

    parser.add_argument("-ns", "--nearlysorted", type = int, help = "uses a nearly sorted list as input", nargs ="?")
    parser.add_argument("-re", "--reversed", help = "uses a reversed listed list as input", action= "store_true")

    args = parser.parse_args()

    l = [randint(0, args.range) for i in range(args.size)]
    if args.nearlysorted:
        b = l[0:ceil(args.size/args.nearlysorted)]
        b.sort()
        l = b + l[ceil(args.size/args.nearlysorted):]
    elif args.reversed:
        l.sort(reverse = True)
    else:
        pass

    temp = l.copy()

    # print(l)

    fig = plt.figure()  # an empty figure with no axes
    fig.suptitle('No axes on this figure')  # Add a title so we know which it is

    fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

    if args.median:
        run('QMSS_module.quickSelectSort(l, 0)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
        l = temp.copy()

    if args.random:
        run('QMSS_module.quickSelectSort(l, 1)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
        l = temp.copy()

    if args.deterministic:
        run('QMSS_module.quickSelectSort(l, 2)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
        l = temp.copy()

    # print(l)

    if args.others:
        # Execution of selectionSort

        run('selectionSort(l)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
        # Execution of insertionSort

        l = temp.copy()

        run('insertionSortDown(l)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

        # Execution of bubbleSort

        l = temp.copy()

        run('bubbleSort(l)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

        # Execution of mergeSort

        l = temp.copy()

        run('mergeSort(l)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

        # Execution of quickSort

        l = temp.copy()

        run('quickSort(l)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

        # Execution of heapSort

        l = temp.copy()

        run('heapSort(l)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

        # Execution of radixSort

        l = temp.copy()

        run('radixSort(l, 100, 10)', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

        # Execution of Sort

        l = temp.copy()

        run('l.sort()', 'stats.txt')
        pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    if not args.median and not args.random and not args.deterministic and not args.others:
        print("No algorithms specified, so  no actions were performed")
        print("use -h, --help flags for help")
