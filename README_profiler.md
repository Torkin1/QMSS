# profiler.py

```
>>> import profiler
>>> help(profiler)
```
```
NAME
   profiler

DESCRIPTION

   File name: profiler.py
   Authors: Mihai Jianu, Daniele La Prova, Lorenzo Mei
   Python version: 3.x

   Script di profiling per gli algoritmi di ordinamento

   $ python3 -m profiler -h

   usage: $ python3 -m profiler [-h] [-m] [-r] [-d] [-o] [-ns [percentage]] [-re]
                             size range

   profiles quickSelectionSort execution time with major sorting algorithms

   positional arguments:
     size                  size of the list
     range                 maximum range of values generated

   optional arguments:
     -h, --help            show this help message and exit
     -m, --median          includes quickSelectSort with sampleMedianSelect
     -r, --random          inlcudes quickSelectSort with quickSelectRand
     -d, --deterministic   includes quickSelectSort with quickSelectDet
     -o, --others          inlcudes major sorting algorithms
     -ns [percentage], --nearlysorted [percentage]
                        uses a list with first size / fraction elements sorted
                        as input
     -re, --reversed       uses a reverse sorted list as input
```
