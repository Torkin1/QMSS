import QMSS_module
import argparse
import cProfile
import pstats
import random
from sorting.Sorting import *


if __name__ == "__main__":

    parser = argparse.ArgumentParser( "python -m main", epilog = "written by Mihai Jianu, Daniele La Prova, Lorenzo Mei", description = "profiles quickSelectionSort execution time with major sorting algorithms")
    
    parser.add_argument("-m", "--median", help = "includes quickSelectSort with sampleMedianSelect", action = "store_true")
    parser.add_argument("-r", "--random", help = "inlcudes quickSelectSort with quickSelectRand", action = "store_true")
    parser.add_argument("-d", "--deterministic", help = "includes quickSelectSort with quickSelectDet", action = "store_true")
    parser.add_argument("size", type = int, help = "size of the list")

    args = parser.parse_args()

    l = [random.randint(0, 100) for i in range(args.size)]
    temp = l.copy()

    #print(l)

    if args.median:

    	cProfile.run('QMSS_module.quickSelectSort(l, 0)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    if args.random:

    	cProfile.run('QMSS_module.quickSelectSort(l, 1)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    if args.deterministic:

    	cProfile.run('QMSS_module.quickSelectSort(l, 2)', 'stats.txt')
    	pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()


    #print(l)

    #Execution of selectionSort

    l = temp.copy()

    cProfile.run('selectionSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of insertionSort

    l = temp.copy()

    cProfile.run('insertionSortDown(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of bubbleSort

    l = temp.copy()

    cProfile.run('bubbleSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of mergeSort

    l = temp.copy()

    cProfile.run('mergeSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of quickSort

    l = temp.copy()

    cProfile.run('quickSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of heapSort

    l = temp.copy()

    cProfile.run('heapSort(l)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of radixSort

    l = temp.copy()

    cProfile.run('radixSort(l, 100, 10)', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()

    #Execution of Sort

    l = temp.copy()

    cProfile.run('l.sort()', 'stats.txt')
    pstats.Stats('stats.txt').strip_dirs().sort_stats("time").print_stats()
